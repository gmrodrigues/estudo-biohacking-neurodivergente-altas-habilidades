"""Audit design degrees of freedom and observable complete-case selection."""
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
import patsy
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
CYCLE1 = OUT.parent / "cycle-001"
CYCLE2 = OUT.parent / "cycle-002"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cycle1 = load_module("cycle001_analysis", CYCLE1 / "run_analysis.py")
cycle2 = load_module("cycle002_audit", CYCLE2 / "run_audit.py")
FORMULAS = {
    "H1": "SLD012 ~ CAFF100 + CAFF_X_AGE + ENERGY1000 + AGE10 + AGE10_SQ + C(SEX) + C(RACE) + C(EDUC) + PIR",
    "H2": "PHQ8_NOSLEEP ~ C(SLEEP_CAT) + SED_HOURS + AGE10 + AGE10_SQ + C(SEX) + C(RACE) + C(EDUC) + PIR",
    "H3": "SLD012 ~ DIET_MAG100 + SUPP_MAG100 + SUPP_MAG_UNQUANT + ENERGY1000 + AGE10 + AGE10_SQ + C(SEX) + C(RACE) + C(EDUC) + PIR",
}
PRIMARY = {
    "H1": ["CAFF100", "CAFF_X_AGE"],
    "H2": ["C(SLEEP_CAT)[T.short]", "C(SLEEP_CAT)[T.long]", "SED_HOURS"],
    "H3": ["DIET_MAG100", "SUPP_MAG100", "SUPP_MAG_UNQUANT"],
}
PUBLIC_LABELS = {
    ("H1", "CAFF100"): "Cafeína / 100 mg",
    ("H1", "CAFF_X_AGE"): "Cafeína × idade",
    ("H2", "C(SLEEP_CAT)[T.short]"): "Sono curto",
    ("H2", "C(SLEEP_CAT)[T.long]"): "Sono longo",
    ("H2", "SED_HOURS"): "Sedentarismo",
    ("H3", "DIET_MAG100"): "Magnésio alimentar",
    ("H3", "SUPP_MAG100"): "Magnésio suplementar",
    ("H3", "SUPP_MAG_UNQUANT"): "Total ausente",
}
PROPENSITY_FORMULA = "complete ~ AGE10 + AGE10_SQ + C(SEX) + C(RACE) + C(SDMVSTRA)"


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.average(np.asarray(values, float), weights=np.asarray(weights, float)))


def kish(weights: np.ndarray) -> float:
    weights = np.asarray(weights, float)
    return float(weights.sum() ** 2 / np.square(weights).sum())


def eligible_domain(frame: pd.DataFrame, joined: pd.Series, weight: str) -> pd.Series:
    return (joined & frame["RIDAGEYR"].between(20, 80) & frame[weight].gt(0)
            & frame["SDMVSTRA"].notna() & frame["SDMVPSU"].notna()
            & frame["SEX"].notna() & frame["RACE"].notna())


def propensity_adjustment(frame: pd.DataFrame, eligible: pd.Series,
                          retained: pd.Series, weight: str) -> dict:
    data = frame.loc[eligible].copy()
    data["complete"] = retained.loc[data.index].astype(int)
    y, x = patsy.dmatrices(PROPENSITY_FORMULA, data, return_type="dataframe",
                           NA_action="raise")
    base = data.loc[x.index, weight].to_numpy(float)
    normalized = base / base.mean()
    fit = sm.GLM(np.asarray(y).ravel(), x, family=sm.families.Binomial(),
                 freq_weights=normalized).fit()
    probability = np.asarray(fit.predict(x), float)
    if np.any((probability <= 0) | (probability >= 1)):
        raise ValueError("Propensity predictions must be strictly between zero and one")
    complete = data.loc[x.index, "complete"].to_numpy(bool)
    inverse = 1 / probability[complete]
    cap = float(np.quantile(inverse, 0.99))
    truncated = np.minimum(inverse, cap)
    complete_index = x.index[complete]
    return {
        "eligible_index": x.index,
        "complete_index": complete_index,
        "probability": probability,
        "inverse": pd.Series(inverse, index=complete_index),
        "truncated_inverse": pd.Series(truncated, index=complete_index),
        "summary": {
            "eligible_n": int(len(data)),
            "complete_n": int(complete.sum()),
            "unweighted_completion_rate": float(complete.mean()),
            "survey_weighted_completion_rate": weighted_mean(complete, base),
            "propensity_min": float(probability.min()),
            "propensity_p01": float(np.quantile(probability, 0.01)),
            "propensity_p50": float(np.quantile(probability, 0.50)),
            "propensity_p99": float(np.quantile(probability, 0.99)),
            "propensity_max": float(probability.max()),
            "inverse_probability_p99_cap": cap,
            "inverse_probability_max": float(inverse.max()),
            "logistic_converged": bool(fit.converged),
            "logistic_rank": int(np.linalg.matrix_rank(x)),
            "logistic_columns": int(x.shape[1]),
        },
    }


def balance_diagnostics(frame: pd.DataFrame, weight: str, propensity: dict) -> dict:
    eligible_index = propensity["eligible_index"]
    complete_index = propensity["complete_index"]
    target = frame.loc[eligible_index]
    complete = frame.loc[complete_index]
    target_weight = target[weight].to_numpy(float)
    base_complete_weight = complete[weight].to_numpy(float)
    adjusted_weight = base_complete_weight * propensity["inverse"].to_numpy(float)
    truncated_weight = base_complete_weight * propensity["truncated_inverse"].to_numpy(float)
    variables = {
        "age_years": target["RIDAGEYR"].to_numpy(float),
        "female": target["SEX"].eq(2).to_numpy(float),
    }
    for code in [2, 3, 4, 6, 7]:
        variables[f"race_{code}_vs_1"] = target["RACE"].eq(code).to_numpy(float)
    rows = []
    positions = target.index.get_indexer(complete_index)
    for name, target_values in variables.items():
        complete_values = target_values[positions]
        target_mean = weighted_mean(target_values, target_weight)
        target_variance = weighted_mean(np.square(target_values - target_mean), target_weight)
        scale = np.sqrt(target_variance)
        if scale == 0:
            continue
        base_mean = weighted_mean(complete_values, base_complete_weight)
        adjusted_mean = weighted_mean(complete_values, adjusted_weight)
        truncated_mean = weighted_mean(complete_values, truncated_weight)
        rows.append({
            "variable": name,
            "target_mean": target_mean,
            "complete_case_mean": base_mean,
            "ipw_mean": adjusted_mean,
            "truncated_ipw_mean": truncated_mean,
            "smd_before": float((base_mean - target_mean) / scale),
            "smd_after": float((adjusted_mean - target_mean) / scale),
            "smd_after_truncation": float((truncated_mean - target_mean) / scale),
        })
    return {
        "rows": rows,
        "max_abs_smd_before": max(abs(row["smd_before"]) for row in rows),
        "max_abs_smd_after": max(abs(row["smd_after"]) for row in rows),
        "max_abs_smd_after_truncation": max(abs(row["smd_after_truncation"]) for row in rows),
        "kish_base_complete_weights": kish(base_complete_weight),
        "kish_ipw_weights": kish(adjusted_weight),
        "kish_truncated_ipw_weights": kish(truncated_weight),
    }


def fit_adjusted(frame: pd.DataFrame, formula: str, base_weight: str,
                 multiplier: pd.Series) -> dict:
    analysis = frame.loc[multiplier.index].copy()
    analysis["SELECTION_WEIGHT"] = analysis[base_weight] * multiplier
    result = cycle1.survey_wls(formula, analysis, "SELECTION_WEIGHT")
    if result["df_design"] != 15:
        raise ValueError(f"Expected 15 design degrees of freedom, got {result['df_design']}")
    return result


def public_model(result: dict) -> dict:
    return {key: value for key, value in result.items()
            if key not in {"beta", "covariance", "used_index"}}


def main() -> None:
    tables = {name: cycle1.read_xpt(name) for name in
              ["DEMO_L", "DR1TOT_L", "SLQ_L", "PAQ_L", "DPQ_L", "DSQTOT_L"]}
    reference = json.loads((CYCLE1 / "results.json").read_text())
    cycle2_results = json.loads((CYCLE2 / "results.json").read_text())
    report = {
        "date": "2026-09-10",
        "scope": "design_df_decision_and_observable_complete_case_selection",
        "diagnostic_groups": "not_assessed",
        "df_decision": {
            "primary": "represented PSUs minus represented strata",
            "primary_df": 15,
            "represented_psus": 30,
            "represented_strata": 15,
            "svy_residual_df_sensitivity": 1,
            "reason": "NCHS defines complex-survey degrees of freedom from represented PSUs minus strata; survey documents residual df as potentially very conservative for individual-level covariates.",
            "whole_model_or_data_driven_term_search": "not_performed",
        },
        "models": {},
        "primary_terms": [],
    }
    for hypothesis in ["H1", "H2", "H3"]:
        frame, joined, retained, _, _, weight = cycle2.prepare(hypothesis, tables)
        eligible = eligible_domain(frame, joined, weight)
        if not retained[~eligible].sum() == 0:
            raise ValueError(f"{hypothesis}: retained cases outside eligible domain")
        propensity = propensity_adjustment(frame, eligible, retained, weight)
        if not propensity["summary"]["logistic_converged"]:
            raise ValueError(f"{hypothesis}: propensity model did not converge")
        balance = balance_diagnostics(frame, weight, propensity)
        ipw = fit_adjusted(frame, FORMULAS[hypothesis], weight, propensity["inverse"])
        truncated = fit_adjusted(frame, FORMULAS[hypothesis], weight,
                                 propensity["truncated_inverse"])
        model = {
            "base_weight": weight,
            "selection_model": PROPENSITY_FORMULA,
            "selection": propensity["summary"],
            "balance": balance,
            "ipw_model": public_model(ipw),
            "truncated_ipw_model": public_model(truncated),
        }
        report["models"][hypothesis] = model
        for term in PRIMARY[hypothesis]:
            original = reference["models"][hypothesis]["coefficients"][term]
            adjusted = ipw["coefficients"][term]
            capped = truncated["coefficients"][term]
            report["primary_terms"].append({
                "model": hypothesis,
                "term": term,
                "reference_estimate": original["estimate"],
                "reference_se": original["se"],
                "ipw_estimate": adjusted["estimate"],
                "ipw_se": adjusted["se"],
                "ipw_ci_low": adjusted["ci_low"],
                "ipw_ci_high": adjusted["ci_high"],
                "ipw_p_value": adjusted["p_value"],
                "truncated_ipw_estimate": capped["estimate"],
                "truncated_ipw_se": capped["se"],
                "absolute_change": adjusted["estimate"] - original["estimate"],
                "relative_change": ((adjusted["estimate"] - original["estimate"])
                                    / abs(original["estimate"])) if original["estimate"] else None,
            })
    adjusted_q = multipletests(
        [row["ipw_p_value"] for row in report["primary_terms"]], method="fdr_bh")[1]
    for row, q_value in zip(report["primary_terms"], adjusted_q):
        row["ipw_q_value"] = float(q_value)
    report["prior_residual_df_sensitivity"] = [
        {key: row[key] for key in ["model", "term", "svy_p", "q_svy_default"]}
        for row in cycle2_results["primary_df_sensitivity"]
    ]
    report["input_sha256"] = reference["input_sha256"]
    report["provenance_sha256"] = {
        str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [Path(__file__), OUT / "protocol.md", OUT / "hypothesis.yaml",
                     CYCLE1 / "run_analysis.py", CYCLE1 / "results.json",
                     CYCLE2 / "run_audit.py", CYCLE2 / "results.json"]
    }
    (OUT / "results.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    make_figures(report)
    print(json.dumps({
        "df_decision": report["df_decision"],
        "selection": {key: value["selection"] for key, value in report["models"].items()},
        "balance": {key: {name: value["balance"][name] for name in
                          ["max_abs_smd_before", "max_abs_smd_after",
                           "kish_base_complete_weights", "kish_ipw_weights"]}
                    for key, value in report["models"].items()},
        "primary_terms": report["primary_terms"],
    }, ensure_ascii=False, indent=2))


def make_figures(report: dict) -> None:
    (OUT / "figures").mkdir(exist_ok=True)
    models = ["H1", "H2", "H3"]
    eligible = [report["models"][name]["selection"]["eligible_n"] for name in models]
    complete = [report["models"][name]["selection"]["complete_n"] for name in models]
    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    positions = np.arange(len(models))
    ax.bar(positions - 0.18, eligible, 0.36, label="Elegíveis 20–80 com peso positivo", color="#93a8ac")
    ax.bar(positions + 0.18, complete, 0.36, label="Casos completos", color="#087e8b")
    for x, total, kept in zip(positions, eligible, complete):
        ax.text(x + 0.18, kept + 70, f"{kept/total:.1%}".replace(".", ","), ha="center")
    ax.set(xticks=positions, xticklabels=models, ylabel="Participantes",
           title="Seleção dentro da população elegível para cada hipótese")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "figures/eligible-complete.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.8))
    for ax, hypothesis in zip(axes, models):
        rows = [row for row in report["primary_terms"] if row["model"] == hypothesis]
        labels = [PUBLIC_LABELS[(hypothesis, row["term"])] for row in rows]
        reference = np.array([row["reference_estimate"] for row in rows])
        adjusted = np.array([row["ipw_estimate"] for row in rows])
        positions = np.arange(len(rows))
        ax.scatter(reference, positions - 0.10, label="Casos completos",
                   color="#6c757d", marker="s")
        ax.scatter(adjusted, positions + 0.10, label="Reponderação",
                   color="#087e8b")
        for y, left, right in zip(positions, reference, adjusted):
            ax.plot([left, right], [y - 0.10, y + 0.10], color="#b8c0c4", linewidth=1)
        ax.axvline(0, color="#555", linestyle="--", linewidth=1)
        ax.set(yticks=positions, yticklabels=labels, xlabel="Coeficiente")
        ax.set_title(hypothesis)
    axes[0].set_ylabel("Contraste registrado")
    axes[-1].legend(loc="best")
    fig.suptitle("Sensibilidade à seleção observável, com escala própria por hipótese")
    fig.tight_layout()
    fig.savefig(OUT / "figures/ipw-coefficients.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
