"""Audit magnesium measurement in NHANES supplement/product files."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
DATA = ROOT / "data/public/nhanes/2021-2023"
CYCLE2 = OUT.parent / "cycle-002/run_audit.py"
spec = importlib.util.spec_from_file_location("cycle002_audit", CYCLE2)
cycle2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cycle2)
ZERO_THRESHOLD = 1e-70


def read_xpt(name: str) -> pd.DataFrame:
    frame = pd.read_sas(DATA / f"{name}.xpt", format="xport")
    for column in frame.select_dtypes(include="number"):
        frame[column] = frame[column].mask(frame[column].abs() < ZERO_THRESHOLD, 0.0)
    for column in frame.select_dtypes(include="object"):
        frame[column] = frame[column].str.decode("utf-8", errors="replace")
    return frame


def boolean_counts(frame: pd.DataFrame, fields: list[str]) -> list[dict]:
    return [
        {**{field: bool(values[i]) for i, field in enumerate(fields)}, "n": int(len(block))}
        for values, block in frame.groupby(fields, dropna=False, observed=True)
    ]


def classify_magnesium_state(row: pd.Series) -> str:
    """Separate quantified, structural-zero, unmatched and unresolved states."""
    if pd.notna(row["DSQTMAGN"]):
        return "quantified_magnesium"
    if row["any_label_magnesium"]:
        return "magnesium_label_but_total_missing"
    if row["any_no_or_unknown_match"]:
        return "no_magnesium_identified_with_unmatched_product"
    if pd.notna(row["reported_records"]):
        return "reported_products_no_magnesium_identified"
    return "no_released_product_record"


def main() -> None:
    tables = {name: read_xpt(name) for name in
              ["DEMO_L", "DR1TOT_L", "DSQTOT_L", "SLQ_L", "DSQIDS_L", "DSPI", "DSII", "DSBI"]}
    ids, totals, products, ingredients = (tables[n] for n in ["DSQIDS_L", "DSQTOT_L", "DSPI", "DSII"])
    if not products["DSDPID"].is_unique:
        raise ValueError("DSPI must contain one record per DSDPID")

    ingredients["magnesium_named"] = ingredients["DSDINGR"].str.contains(
        "MAGNES", case=False, na=False)
    ingredients["elemental_magnesium"] = ingredients["DSDINGR"].str.fullmatch(
        "MAGNESIUM", case=False, na=False)
    product_flags = ingredients.groupby("DSDPID", observed=True).agg(
        label_has_magnesium=("magnesium_named", "any"),
        label_has_elemental_magnesium=("elemental_magnesium", "any"),
        ingredient_rows=("DSDIID", "size"),
    )
    records = ids.merge(products[["DSDPID", "DSDPRDT", "DSDTYPE"]], on="DSDPID",
                        how="left", validate="many_to_one", indicator="product_merge")
    records = records.merge(product_flags, left_on="DSDPID", right_index=True,
                            how="left", validate="many_to_one")
    for column in ["label_has_magnesium", "label_has_elemental_magnesium"]:
        records[column] = records[column].fillna(False).astype(bool)
    records["calculated_magnesium"] = records["DSQIMAGN"].notna()
    records["antacid"] = records["DSDANTA"].isin([1, 2])
    records["valid_days"] = records["DSD103"].between(1, 30)
    records["valid_quantity"] = records["DSD122Q"].between(0, 120)
    records["serving_ratio_present"] = records["DSDACTSS"].notna()
    records["no_or_unknown_match"] = records["DSDMTCH"].isin([6, 9])

    person = records.groupby("SEQN", observed=True).agg(
        reported_records=("DSDPID", "size"),
        any_label_magnesium=("label_has_magnesium", "any"),
        any_elemental_magnesium=("label_has_elemental_magnesium", "any"),
        any_calculated_magnesium=("calculated_magnesium", "any"),
        any_antacid=("antacid", "any"),
        any_no_or_unknown_match=("no_or_unknown_match", "any"),
        all_no_or_unknown_match=("no_or_unknown_match", "all"),
        any_invalid_days=("valid_days", lambda s: (~s).any()),
        any_invalid_quantity=("valid_quantity", lambda s: (~s).any()),
        any_missing_serving_ratio=("serving_ratio_present", lambda s: (~s).any()),
    )
    person = totals.merge(person, left_on="SEQN", right_index=True, how="left",
                          validate="one_to_one")
    bool_fields = [column for column in person if column.startswith("any_") or column.startswith("all_")]
    person[bool_fields] = person[bool_fields].fillna(False).astype(bool)

    # Recreate the exact H3 complete-case participants from cycle 001/002.
    audit_tables = {name: tables[name] for name in ["DEMO_L", "DR1TOT_L", "DSQTOT_L", "SLQ_L"]}
    h3_frame, _, h3_retained, _, _, _ = cycle2.prepare("H3", audit_tables)
    h3_ids = set(h3_frame.loc[h3_retained, "SEQN"])
    h3 = person[person["SEQN"].isin(h3_ids)].copy()
    if len(h3) != 4194:
        raise ValueError(f"Expected 4194 H3 participants, got {len(h3)}")

    h3["magnesium_state"] = h3.apply(classify_magnesium_state, axis=1)
    state_counts = h3["magnesium_state"].value_counts().to_dict()

    # Official totals are rounded to one decimal after frequency adjustment.
    records["reconstructed_daily_magnesium"] = (
        records["DSQIMAGN"] * records["DSD103"].where(records["valid_days"]) / 30
    )
    reconstructed = records.groupby("SEQN", observed=True)["reconstructed_daily_magnesium"].sum(min_count=1)
    comparison = totals[["SEQN", "DSQTMAGN"]].merge(
        reconstructed.rename("reconstructed"), left_on="SEQN", right_index=True, how="left")
    both = comparison.dropna(subset=["DSQTMAGN", "reconstructed"]).copy()
    both["absolute_difference"] = (both["DSQTMAGN"] - both["reconstructed"]).abs()
    reconstruction = {
        "both_present_n": int(len(both)),
        "exact_before_rounding_n": int(np.isclose(both["absolute_difference"], 0, atol=1e-12).sum()),
        "within_half_of_0_1_unit_n": int((both["absolute_difference"] <= 0.0500000001).sum()),
        "max_absolute_difference_before_rounding": float(both["absolute_difference"].max()),
    }
    if reconstruction["within_half_of_0_1_unit_n"] != len(both):
        raise ValueError("Individual magnesium does not reconstruct total within 0.05 mg")

    h3_records = records[records["SEQN"].isin(h3_ids)].copy()
    ambiguous_records = h3_records[
        h3_records["label_has_magnesium"] & ~h3_records["calculated_magnesium"]]
    no_supplement_with_magnesium = h3[(h3["DSD010"] == 2) & h3["DSQTMAGN"].notna()]
    if not no_supplement_with_magnesium["any_antacid"].all():
        raise ValueError("Expected quantified magnesium among DSD010=2 to come from antacid records")

    result = {
        "date": "2026-09-09",
        "scope": "measurement_audit_no_outcome_model",
        "diagnostic_groups": "not_assessed",
        "file_inventory": {
            name: {"rows": int(len(frame)), "columns": int(len(frame.columns)),
                   "sha256": hashlib.sha256((DATA / f"{name}.xpt").read_bytes()).hexdigest()}
            for name, frame in tables.items()
        },
        "joins": {
            "DSPI_unique_DSDPID": bool(products["DSDPID"].is_unique),
            "DSQIDS_rows": int(len(ids)),
            "DSQIDS_participants": int(ids["SEQN"].nunique()),
            "DSQIDS_unique_products": int(ids["DSDPID"].nunique()),
            "product_match_rows": int((records["product_merge"] == "both").sum()),
            "product_unmatched_rows": int((records["product_merge"] != "both").sum()),
            "ingredient_match_rows": int(records["ingredient_rows"].notna().sum()),
        },
        "codebook_totals": {
            "records_non_antacid": int((ids["DSDANTA"] == 0).sum()),
            "records_antacid_supplement_section": int((ids["DSDANTA"] == 1).sum()),
            "records_antacid_antacid_section": int((ids["DSDANTA"] == 2).sum()),
            "exact_near_exact_match": int((ids["DSDMTCH"] == 1).sum()),
            "no_match": int((ids["DSDMTCH"] == 6).sum()),
            "dont_know_match": int((ids["DSDMTCH"] == 9).sum()),
            "individual_magnesium_present": int(ids["DSQIMAGN"].notna().sum()),
        },
        "reconstruction": reconstruction,
        "h3": {
            "n": int(len(h3)),
            "state_counts": {str(key): int(value) for key, value in state_counts.items()},
            "legacy_unquantified_indicator_n": int(((h3["DSD010"] == 1) & h3["DSQTMAGN"].isna()).sum()),
            "magnesium_label_but_total_missing_n": int((h3["magnesium_state"] == "magnesium_label_but_total_missing").sum()),
            "DSD010_no_but_magnesium_quantified_n": int(len(no_supplement_with_magnesium)),
            "DSD010_no_but_magnesium_quantified_all_antacid": bool(no_supplement_with_magnesium["any_antacid"].all()),
            "record_level_magnesium_label_amount_missing_n": int(len(ambiguous_records)),
            "record_level_ambiguity": boolean_counts(
                ambiguous_records,
                ["antacid", "valid_days", "valid_quantity", "serving_ratio_present", "no_or_unknown_match"]),
            "classification_by_DSD010": [
                {"DSD010": None if pd.isna(code) else int(code), "state": str(state), "n": int(len(block))}
                for (code, state), block in h3.groupby(["DSD010", "magnesium_state"], dropna=False, observed=True)
            ],
        },
        "limitations": [
            "Dados de rótulo não comprovam ingestão ou adesão.",
            "Nomes de ingredientes com magnésio não fornecem, sozinhos, a quantidade elementar.",
            "Nomes comerciais não são apropriados para prevalência e não são publicados aqui.",
            "Misturas foram inventariadas, sem inferir magnésio oculto.",
            "Mesmos participantes e onda do ciclo 001; sem novo modelo de desfecho ou replicação.",
        ],
    }
    result["provenance_sha256"] = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [Path(__file__), OUT / "protocol.md", OUT.parent / "cycle-001/run_analysis.py",
                     OUT.parent / "cycle-001/results.json"]
    }
    (OUT / "results.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    make_figures(result)
    print(json.dumps({"joins": result["joins"], "h3": result["h3"],
                      "reconstruction": reconstruction}, ensure_ascii=False, indent=2))


def make_figures(result: dict) -> None:
    OUT.joinpath("figures").mkdir(exist_ok=True)
    states = result["h3"]["state_counts"]
    order = ["quantified_magnesium", "reported_products_no_magnesium_identified",
             "no_magnesium_identified_with_unmatched_product",
             "magnesium_label_but_total_missing", "no_released_product_record"]
    labels = ["Magnésio quantificado", "Produtos sem magnésio identificado",
              "Produto sem correspondência; magnésio não identificado",
              "Rótulo com magnésio, total ausente", "Sem registro de produto liberado"]
    values = [states.get(key, 0) for key in order]
    fig, ax = plt.subplots(figsize=(10, 5.8))
    bars = ax.barh(labels[::-1], values[::-1], color=["#087e8b", "#93a8ac", "#e98436", "#c44e52", "#c4cbd0"][::-1])
    for bar, value in zip(bars, values[::-1]):
        ax.text(bar.get_width() + 18, bar.get_y() + bar.get_height()/2,
                f"{value:,}".replace(",", "."), va="center")
    ax.set(xlabel="Participantes de H3 (contagem não ponderada)",
           title="O valor ausente de DSQTMAGN reúne estados diferentes\nNHANES 2021–2023, H3 n=4.194")
    ax.set_xlim(0, max(values) * 1.17)
    fig.tight_layout()
    fig.savefig(OUT / "figures/magnesium-states.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
