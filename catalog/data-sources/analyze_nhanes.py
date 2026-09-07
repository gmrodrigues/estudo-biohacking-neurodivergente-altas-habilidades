"""Profile the public NHANES tables used in the feasibility analysis."""

from pathlib import Path

import pandas as pd


DATA_DIR = Path("data/public/nhanes/2021-2023")
CORE_FILES = ("DEMO_L", "DSQTOT_L", "PAQ_L", "SLQ_L")
EXTENDED_FILES = (
    "DR1TOT_L",
    "BMX_L",
    "DPQ_L",
    "VID_L",
    "BPXO_L",
)
FILES = CORE_FILES + EXTENDED_FILES


def read_xpt(name: str) -> pd.DataFrame:
    frame = pd.read_sas(DATA_DIR / f"{name}.xpt", format="xport")
    # Numeric zero in these SAS XPORT files can be decoded by pandas as the
    # smallest positive IBM-format float. Normalize it before summaries.
    numeric = frame.select_dtypes(include="number").columns
    frame[numeric] = frame[numeric].mask(frame[numeric].abs() < 1e-70, 0.0)
    return frame


def main() -> None:
    frames = {name: read_xpt(name) for name in FILES}

    for name, frame in frames.items():
        print(
            f"{name}: rows={len(frame)}, columns={len(frame.columns)}, "
            f"participants={frame['SEQN'].nunique()}"
        )

    core_ids = set.intersection(
        *(set(frames[name]["SEQN"].dropna()) for name in CORE_FILES)
    )
    shared_ids = set.intersection(*(set(frame["SEQN"].dropna()) for frame in frames.values()))
    cohort = frames["DEMO_L"][frames["DEMO_L"]["SEQN"].isin(shared_ids)]
    ages = cohort["RIDAGEYR"]

    print(f"core_shared_participants={len(core_ids)}")
    print(f"extended_shared_participants={len(shared_ids)}")
    print(f"age_min={ages.min():.0f}")
    print(f"age_median={ages.median():.0f}")
    print(f"age_max={ages.max():.0f}")
    print(f"participants_under_18={(ages < 18).sum()}")

    supplement = frames["DSQTOT_L"]
    print(f"supplement_count_observed={supplement['DSDCOUNT'].notna().sum()}")
    print(f"supplement_count_median={supplement['DSDCOUNT'].median():.0f}")

    selected = {
        "DEMO_L": ["RIDAGEYR", "RIAGENDR", "DMDEDUC2", "INDFMPIR"],
        "DSQTOT_L": ["DSDCOUNT", "DSQTVD", "DSQTMAGN", "DSQTIRON", "DSQTCAFF"],
        "DR1TOT_L": ["DR1TKCAL", "DR1TPROT", "DR1TCARB", "DR1TFIBE", "DR1TCAFF"],
        "SLQ_L": ["SLD012", "SLD013"],
        "PAQ_L": ["PAD790Q", "PAD800", "PAD810Q", "PAD820", "PAD680"],
        "BMX_L": ["BMXBMI", "BMXWAIST"],
        "VID_L": ["LBXVIDMS"],
        "BPXO_L": ["BPXOSY1", "BPXOSY2", "BPXOSY3", "BPXODI1", "BPXODI2", "BPXODI3"],
        "DPQ_L": [f"DPQ0{i}0" for i in range(1, 10)],
    }
    merged = frames["DEMO_L"][["SEQN"] + selected["DEMO_L"]]
    for name, columns in selected.items():
        if name == "DEMO_L":
            continue
        merged = merged.merge(frames[name][["SEQN"] + columns], on="SEQN", how="inner")

    phq_columns = selected["DPQ_L"]
    valid_phq = merged[phq_columns].where(merged[phq_columns].isin([0, 1, 2, 3]))
    merged["PHQ9_TOTAL"] = valid_phq.sum(axis=1, min_count=9)
    merged["SYSTOLIC_MEAN"] = merged[["BPXOSY1", "BPXOSY2", "BPXOSY3"]].mean(axis=1)
    merged["DIASTOLIC_MEAN"] = merged[["BPXODI1", "BPXODI2", "BPXODI3"]].mean(axis=1)

    print("selected_variable_completeness")
    for column in (
        "DSDCOUNT", "DSQTVD", "DSQTMAGN", "DR1TKCAL", "DR1TPROT",
        "SLD012", "SLD013", "PAD680", "BMXBMI", "LBXVIDMS",
        "PHQ9_TOTAL", "SYSTOLIC_MEAN", "DIASTOLIC_MEAN",
    ):
        observed = int(merged[column].notna().sum())
        print(f"{column}={observed}/{len(merged)} ({observed / len(merged):.1%})")


if __name__ == "__main__":
    main()
