"""Compare original/corrected cycle 001 results and write aggregate audit artifacts."""

import hashlib
import json
from pathlib import Path

import numpy as np
from statsmodels.stats.multitest import multipletests

from run_analysis import merge_tables, prepare_demographics


OUT = Path(__file__).resolve().parent
AMENDMENT = OUT / "amendments/h2-boundary-2026-09-09"
TERMS = {
    "H1_caffeine": ("H1", "CAFF100"),
    "H1_caffeine_x_age": ("H1", "CAFF_X_AGE"),
    "H2_short_sleep": ("H2", "C(SLEEP_CAT)[T.short]"),
    "H2_long_sleep": ("H2", "C(SLEEP_CAT)[T.long]"),
    "H2_sedentary": ("H2", "SED_HOURS"),
    "H3_diet_magnesium": ("H3", "DIET_MAG100"),
    "H3_supplement_magnesium": ("H3", "SUPP_MAG100"),
    "H3_supplement_unquantified": ("H3", "SUPP_MAG_UNQUANT"),
}


def main():
    original_path = AMENDMENT / "results-original.json"
    corrected_path = OUT / "results.json"
    old = json.loads(original_path.read_text())
    new = json.loads(corrected_path.read_text())
    checks = {key: old["models"][key] == new["models"][key]
              for key in ["H1", "H1_sensitivity", "H3"]}
    checks.update({key: old[key] == new[key] for key in ["prediction", "input_sha256"]})
    checks["original_audit_fields"] = all(new["audit"][k] == v for k, v in old["audit"].items())

    # Reconstruct the complete-case cohort independently of Patsy's model matrix.
    cohort = prepare_demographics(merge_tables(["DEMO_L", "SLQ_L", "PAQ_L", "DPQ_L"]))
    items = ["DPQ010", "DPQ020", "DPQ040", "DPQ050", "DPQ060", "DPQ070", "DPQ080", "DPQ090"]
    complete = (cohort[items].isin([0, 1, 2, 3]).all(axis=1)
                & cohort["PAD680"].between(0, 1380) & cohort["WTMEC2YR"].gt(0)
                & cohort[["SLD012", "AGE10", "SEX", "RACE", "EDUC", "PIR",
                           "SDMVSTRA", "SDMVPSU"]].notna().all(axis=1))
    used = cohort.loc[complete]
    sleep = used["SLD012"]
    counts_old = {"short": int(sleep.le(7).sum()), "recommended": int((sleep.gt(7) & sleep.le(9)).sum()),
                  "long": int(sleep.gt(9).sum())}
    counts_new = {"short": int(sleep.lt(7).sum()), "recommended": int(sleep.between(7, 9).sum()),
                  "long": int(sleep.gt(9).sum())}
    checks["cohort_n"] = len(used) == new["models"]["H2"]["n"]
    checks["category_counts"] = counts_new == new["audit"]["H2_sleep_counts"]
    checks["reclassified_n"] = int(sleep.eq(7).sum()) == new["audit"]["H2_exactly_7h_reclassified"]
    rows = []
    for name, (model, term) in TERMS.items():
        a, b = old["models"][model]["coefficients"][term], new["models"][model]["coefficients"][term]
        rows.append({"term": name, "original": {**a, "q": old["primary_fdr"][name]},
                     "corrected": {**b, "q": new["primary_fdr"][name]},
                     "estimate_delta": b["estimate"] - a["estimate"],
                     "q_delta": new["primary_fdr"][name] - old["primary_fdr"][name]})
    expected = multipletests([row["corrected"]["p_value"] for row in rows], method="fdr_bh")[1]
    checks["fdr_matches_statsmodels"] = bool(np.allclose(expected, [r["corrected"]["q"] for r in rows],
                                                        rtol=1e-12, atol=0))
    if not all(checks.values()):
        raise ValueError(f"Amendment invariant failed: {checks}")
    files = [original_path, corrected_path, OUT / "run_analysis.py", AMENDMENT / "protocol.md"]
    report = {"date": "2026-09-09", "original_commit": "3a4eec48a45e1d29ac670663ae4187cbe9a2e087",
              "checks": checks, "sha256": {str(p.relative_to(OUT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
              "category_counts_original": counts_old, "category_counts_corrected": counts_new,
              "reclassified_exactly_7h": int(sleep.eq(7).sum()), "n": len(used), "terms": rows}
    (AMENDMENT / "comparison.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    lines = ["# Auditoria da correção H2 — 2026-09-09", "",
             "[Decisão anterior à reexecução](protocol.md) · [Execução original](results-original.json) · [Comparação completa e hashes](comparison.json)", "",
             f"Amostra preservada: {len(used):,} participantes. Exatamente {int(sleep.eq(7).sum())} pessoas com 7 h passaram do grupo curto à referência.", "",
             "| Grupo | Original: ≤7 / >7–≤9 / >9 | Corrigido: <7 / 7–9 / >9 |", "|---|---:|---:|"]
    lines += [f"| {key} | {counts_old[key]} | {counts_new[key]} |" for key in counts_old]
    lines += ["", "| Termo | Estimativa original [IC95%] | Corrigida [IC95%] | p original → corrigido | q original → corrigido |",
              "|---|---|---|---|---|"]
    for row in rows:
        a, b = row["original"], row["corrected"]
        lines.append(f"| {row['term']} | {a['estimate']:+.6f} [{a['ci_low']:+.6f}, {a['ci_high']:+.6f}] | "
                     f"{b['estimate']:+.6f} [{b['ci_low']:+.6f}, {b['ci_high']:+.6f}] | "
                     f"{a['p_value']:.8g} → {b['p_value']:.8g} | {a['q']:.8g} → {b['q']:.8g} |")
    lines += ["", "H1/H3: horas de sono; H2: pontos no escore de sintomas sem sono (0–24), sedentarismo por hora/dia.", "",
              "Os três termos de H2 permanecem positivos e com IC95% acima de zero. O contraste curto aumentou, o longo diminuiu; o estimando mudou porque 7 h passou à referência registrada. Isso não é replicação ou evidência causal.", "",
              "Todos os oito q-valores foram recalculados; apenas os três de H2 mudaram. H1, sua sensibilidade, H3, previsão, campos originais da auditoria e hashes de insumos reproduziram exatamente a execução original. A checagem independente de FDR com statsmodels passou. A variância de desenho ainda requer validação externa.", "",
              "Comandos, a partir da raiz:", "", "```bash",
              "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/run_analysis.py",
              "MPLCONFIGDIR=/tmp/science-matplotlib PIPENV_VENV_IN_PROJECT=1 pipenv run python research/discoveries/cycle-001/audit_h2_amendment.py", "```", ""]
    (AMENDMENT / "audit.md").write_text("\n".join(lines))
    print(json.dumps({"checks": checks, "n": len(used), "reclassified": int(sleep.eq(7).sum())}, indent=2))


if __name__ == "__main__":
    main()
