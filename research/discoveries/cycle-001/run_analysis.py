"""Execute cycle 001 analyses on public NHANES 2021-2023 data."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import patsy
from scipy import stats
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "data/public/nhanes/2021-2023"
OUT = Path(__file__).resolve().parent
FIGURES = OUT / "figures"
ZERO_THRESHOLD = 1e-70
SEED = 20260907


def read_xpt(name: str) -> pd.DataFrame:
    frame = pd.read_sas(DATA / f"{name}.xpt", format="xport")
    numeric = frame.select_dtypes(include="number").columns
    frame[numeric] = frame[numeric].mask(frame[numeric].abs() < ZERO_THRESHOLD, 0.0)
    return frame


def merge_tables(names: list[str]) -> pd.DataFrame:
    frames = [read_xpt(name) for name in names]
    result = frames[0]
    for frame in frames[1:]:
        if not result["SEQN"].is_unique or not frame["SEQN"].is_unique:
            raise ValueError("Expected one row per participant before joining")
        duplicates = sorted((set(result.columns) & set(frame.columns)) - {"SEQN"})
        result = result.merge(frame, on="SEQN", how="inner", validate="one_to_one",
                              suffixes=("", "__duplicate"))
        for column in duplicates:
            duplicate = f"{column}__duplicate"
            left = result[column].fillna(-np.inf)
            right = result[duplicate].fillna(-np.inf)
            if not np.allclose(left, right):
                raise ValueError(f"Conflicting duplicate column after join: {column}")
            result = result.drop(columns=duplicate)
    return result


def prepare_demographics(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    result = result[result["RIDAGEYR"] >= 18]
    result["AGE10"] = (result["RIDAGEYR"] - 45.0) / 10.0
    result["AGE10_SQ"] = result["AGE10"] ** 2
    result["SEX"] = result["RIAGENDR"].where(result["RIAGENDR"].isin([1, 2]))
    result["RACE"] = result["RIDRETH3"].where(result["RIDRETH3"].isin([1, 2, 3, 4, 6, 7]))
    result["EDUC"] = result["DMDEDUC2"].where(result["DMDEDUC2"].isin([1, 2, 3, 4, 5]))
    result["PIR"] = result["INDFMPIR"].where(result["INDFMPIR"].between(0, 5))
    return result


def survey_wls(formula: str, frame: pd.DataFrame, weight: str) -> dict:
    """Weighted least squares with stratified-PSU linearized covariance."""
    y_df, x_df = patsy.dmatrices(formula, frame, return_type="dataframe", NA_action="drop")
    used = frame.loc[x_df.index].copy()
    valid = used[weight].gt(0) & used["SDMVSTRA"].notna() & used["SDMVPSU"].notna()
    y = np.asarray(y_df.loc[valid]).ravel()
    x = np.asarray(x_df.loc[valid])
    used = used.loc[valid]
    w = used[weight].to_numpy(float)
    xtwx = x.T @ (w[:, None] * x)
    bread = np.linalg.pinv(xtwx)
    beta = bread @ (x.T @ (w * y))
    residual = y - x @ beta
    scores = w[:, None] * x * residual[:, None]
    score_frame = pd.DataFrame(scores, columns=x_df.columns, index=used.index)
    score_frame["stratum"] = used["SDMVSTRA"].to_numpy()
    score_frame["psu"] = used["SDMVPSU"].to_numpy()
    grouped = score_frame.groupby(["stratum", "psu"], observed=True)[list(x_df.columns)].sum()
    meat = np.zeros((x.shape[1], x.shape[1]))
    strata_used = 0
    psus_used = 0
    for _, block in grouped.groupby(level=0):
        values = block.to_numpy()
        m = len(values)
        if m < 2:
            continue
        centered = values - values.mean(axis=0)
        meat += (m / (m - 1)) * centered.T @ centered
        strata_used += 1
        psus_used += m
    covariance = bread @ meat @ bread
    se = np.sqrt(np.clip(np.diag(covariance), 0, None))
    df = psus_used - strata_used
    critical = stats.t.ppf(0.975, df)
    t_value = np.divide(beta, se, out=np.full_like(beta, np.nan), where=se > 0)
    p_value = 2 * stats.t.sf(np.abs(t_value), df)
    coefficients = {
        name: {"estimate": float(beta[i]), "se": float(se[i]),
               "ci_low": float(beta[i] - critical * se[i]),
               "ci_high": float(beta[i] + critical * se[i]),
               "p_value": float(p_value[i])}
        for i, name in enumerate(x_df.columns)
    }
    return {"formula": formula, "n": len(used), "df_design": df,
            "strata": strata_used, "psus": psus_used,
            "coefficients": coefficients, "beta": beta, "covariance": covariance,
            "columns": list(x_df.columns), "used_index": used.index.tolist()}


def bh_fdr(p_values: dict[str, float]) -> dict[str, float]:
    items = sorted(p_values.items(), key=lambda item: item[1])
    count = len(items)
    adjusted = {}
    running = 1.0
    for rank_from_end, (name, value) in enumerate(reversed(items), start=1):
        rank = count - rank_from_end + 1
        running = min(running, value * count / rank)
        adjusted[name] = float(running)
    return adjusted


def coefficient_plot(model: dict, terms: list[tuple[str, str]], title: str,
                     xlabel: str, path: Path) -> None:
    labels, estimates, lows, highs = [], [], [], []
    for term, label in terms:
        row = model["coefficients"][term]
        labels.append(label)
        estimates.append(row["estimate"])
        lows.append(row["ci_low"])
        highs.append(row["ci_high"])
    positions = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(9, max(3.5, 0.75 * len(labels))))
    ax.errorbar(estimates, positions,
                xerr=[np.array(estimates) - np.array(lows), np.array(highs) - np.array(estimates)],
                fmt="o", capsize=4, color="#087e8b")
    ax.axvline(0, color="#555", linestyle="--", linewidth=1)
    ax.set_yticks(positions, labels)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.grid(axis="x", alpha=0.2)
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    base = read_xpt("DEMO_L")

    h1 = prepare_demographics(merge_tables(["DEMO_L", "DR1TOT_L", "SLQ_L"]))
    h1["CAFF100"] = h1["DR1TCAFF"] / 100.0
    h1["ENERGY1000"] = h1["DR1TKCAL"] / 1000.0
    h1["CAFF_X_AGE"] = h1["CAFF100"] * h1["AGE10"]
    common = "AGE10 + AGE10_SQ + C(SEX) + C(RACE) + C(EDUC) + PIR"
    m1 = survey_wls(f"SLD012 ~ CAFF100 + CAFF_X_AGE + ENERGY1000 + {common}", h1, "WTDRD1")
    h1_sens = h1[h1["DR1TCAFF"].le(800)]
    m1_sensitivity = survey_wls(f"SLD012 ~ CAFF100 + CAFF_X_AGE + ENERGY1000 + {common}", h1_sens, "WTDRD1")

    h2 = prepare_demographics(merge_tables(["DEMO_L", "SLQ_L", "PAQ_L", "DPQ_L"]))
    phq_items = ["DPQ010", "DPQ020", "DPQ040", "DPQ050", "DPQ060", "DPQ070", "DPQ080", "DPQ090"]
    valid_items = h2[phq_items].where(h2[phq_items].isin([0, 1, 2, 3]))
    h2["PHQ8_NOSLEEP"] = valid_items.sum(axis=1, min_count=8)
    h2["SED_HOURS"] = h2["PAD680"].where(h2["PAD680"].between(0, 1380)) / 60.0
    h2["SLEEP_CAT"] = pd.cut(h2["SLD012"], [-np.inf, 7, 9, np.inf], right=True,
                             labels=["short", "recommended", "long"])
    h2["SLEEP_CAT"] = h2["SLEEP_CAT"].cat.reorder_categories(["recommended", "short", "long"])
    m2 = survey_wls(f"PHQ8_NOSLEEP ~ C(SLEEP_CAT) + SED_HOURS + {common}", h2, "WTMEC2YR")

    h3 = prepare_demographics(merge_tables(["DEMO_L", "DR1TOT_L", "DSQTOT_L", "SLQ_L"]))
    h3["DIET_MAG100"] = h3["DR1TMAGN"] / 100.0
    h3["ENERGY1000"] = h3["DR1TKCAL"] / 1000.0
    h3["SUPP_MAG_UNQUANT"] = ((h3["DSD010"] == 1) & h3["DSQTMAGN"].isna()).astype(float)
    h3["SUPP_MAG100"] = h3["DSQTMAGN"].fillna(0) / 100.0
    h3.loc[~h3["DSD010"].isin([1, 2]), ["SUPP_MAG100", "SUPP_MAG_UNQUANT"]] = np.nan
    m3 = survey_wls(f"SLD012 ~ DIET_MAG100 + SUPP_MAG100 + SUPP_MAG_UNQUANT + ENERGY1000 + {common}", h3, "WTDRD1")

    primary_p = {
        "H1_caffeine": m1["coefficients"]["CAFF100"]["p_value"],
        "H1_caffeine_x_age": m1["coefficients"]["CAFF_X_AGE"]["p_value"],
        "H2_short_sleep": m2["coefficients"]["C(SLEEP_CAT)[T.short]"]["p_value"],
        "H2_long_sleep": m2["coefficients"]["C(SLEEP_CAT)[T.long]"]["p_value"],
        "H2_sedentary": m2["coefficients"]["SED_HOURS"]["p_value"],
        "H3_diet_magnesium": m3["coefficients"]["DIET_MAG100"]["p_value"],
        "H3_supplement_magnesium": m3["coefficients"]["SUPP_MAG100"]["p_value"],
        "H3_supplement_unquantified": m3["coefficients"]["SUPP_MAG_UNQUANT"]["p_value"],
    }
    fdr = bh_fdr(primary_p)

    # Cross-sectional diagnosis-agnostic prediction in participants not seen in training.
    prediction = h2.dropna(subset=["PHQ8_NOSLEEP", "SLD012", "SED_HOURS", "RIDAGEYR",
                                   "SEX", "RACE", "EDUC", "PIR", "WTMEC2YR"]).copy()
    features = ["SLD012", "SED_HOURS", "RIDAGEYR", "SEX", "RACE", "EDUC", "PIR"]
    train, test = train_test_split(prediction, test_size=0.25, random_state=SEED,
                                   stratify=(prediction["PHQ8_NOSLEEP"] >= 5))
    numeric = ["SLD012", "SED_HOURS", "RIDAGEYR", "PIR"]
    categorical = ["SEX", "RACE", "EDUC"]
    prep = ColumnTransformer([
        ("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                          ("scale", StandardScaler())]), numeric),
        ("cat", OneHotEncoder(handle_unknown="ignore", drop="first", sparse_output=False), categorical),
    ])
    ridge = Pipeline([("prep", prep), ("model", RidgeCV(alphas=np.logspace(-3, 3, 25)))])
    ridge.fit(train[features], train["PHQ8_NOSLEEP"], model__sample_weight=train["WTMEC2YR"])
    predicted = ridge.predict(test[features])
    baseline_value = np.average(train["PHQ8_NOSLEEP"], weights=train["WTMEC2YR"])
    baseline = np.full(len(test), baseline_value)
    test_weight = test["WTMEC2YR"].to_numpy()
    metrics = {
        "n_train": len(train), "n_test": len(test), "random_seed": SEED,
        "target": "PHQ8_NOSLEEP_0_24_cross_sectional",
        "ridge_alpha": float(ridge.named_steps["model"].alpha_),
        "baseline": {
            "mae": float(mean_absolute_error(test["PHQ8_NOSLEEP"], baseline, sample_weight=test_weight)),
            "rmse": float(mean_squared_error(test["PHQ8_NOSLEEP"], baseline, sample_weight=test_weight) ** 0.5),
            "r2": float(r2_score(test["PHQ8_NOSLEEP"], baseline, sample_weight=test_weight)),
        },
        "ridge": {
            "mae": float(mean_absolute_error(test["PHQ8_NOSLEEP"], predicted, sample_weight=test_weight)),
            "rmse": float(mean_squared_error(test["PHQ8_NOSLEEP"], predicted, sample_weight=test_weight) ** 0.5),
            "r2": float(r2_score(test["PHQ8_NOSLEEP"], predicted, sample_weight=test_weight)),
        },
        "validation": "single_internal_holdout; no_external_or_temporal_validation",
    }
    ablations = {}
    feature_groups = {
        "sleep": ["SLD012"],
        "sedentary": ["SED_HOURS"],
        "demographic_context": ["RIDAGEYR", "SEX", "RACE", "EDUC", "PIR"],
    }
    for group, excluded in feature_groups.items():
        keep_numeric = [column for column in numeric if column not in excluded]
        keep_categorical = [column for column in categorical if column not in excluded]
        keep_features = keep_numeric + keep_categorical
        transformers = []
        if keep_numeric:
            transformers.append(("num", Pipeline([("impute", SimpleImputer(strategy="median")),
                                                   ("scale", StandardScaler())]), keep_numeric))
        if keep_categorical:
            transformers.append(("cat", OneHotEncoder(handle_unknown="ignore", drop="first",
                                                       sparse_output=False), keep_categorical))
        ablated = Pipeline([("prep", ColumnTransformer(transformers)),
                            ("model", RidgeCV(alphas=np.logspace(-3, 3, 25)))])
        ablated.fit(train[keep_features], train["PHQ8_NOSLEEP"],
                    model__sample_weight=train["WTMEC2YR"])
        ablated_prediction = ablated.predict(test[keep_features])
        ablated_rmse = mean_squared_error(test["PHQ8_NOSLEEP"], ablated_prediction,
                                          sample_weight=test_weight) ** 0.5
        ablations[group] = {"rmse_without_group": float(ablated_rmse),
                            "delta_rmse_vs_full": float(ablated_rmse - metrics["ridge"]["rmse"])}
    metrics["domain_ablation"] = ablations

    coefficient_plot(m1, [("CAFF100", "Cafeína, por 100 mg"),
                          ("CAFF_X_AGE", "Cafeína × idade, por década")],
                     "Cafeína e duração habitual do sono", "Diferença ajustada em horas de sono (IC 95%)",
                     FIGURES / "caffeine-sleep.png")
    coefficient_plot(m2, [("C(SLEEP_CAT)[T.short]", "Sono curto (<7 h)"),
                          ("C(SLEEP_CAT)[T.long]", "Sono longo (>9 h)"),
                          ("SED_HOURS", "Sedentarismo, por hora/dia")],
                     "Sono, sedentarismo e sintomas depressivos sem item de sono",
                     "Diferença ajustada no escore PHQ-8 modificado (IC 95%)",
                     FIGURES / "sleep-sedentary-depression.png")
    coefficient_plot(m3, [("DIET_MAG100", "Magnésio alimentar, por 100 mg"),
                          ("SUPP_MAG100", "Magnésio de suplementos, por 100 mg"),
                          ("SUPP_MAG_UNQUANT", "Uso com magnésio não quantificado")],
                     "Magnésio e duração habitual do sono", "Diferença ajustada em horas de sono (IC 95%)",
                     FIGURES / "magnesium-sleep.png")

    plot_frame = pd.DataFrame({"observed": test["PHQ8_NOSLEEP"].to_numpy(), "predicted": predicted,
                               "weight": test_weight})
    plot_frame["decile"] = pd.qcut(plot_frame["predicted"], 10, duplicates="drop")
    calibration = plot_frame.groupby("decile", observed=True).apply(
        lambda block: pd.Series({"predicted": np.average(block["predicted"], weights=block["weight"]),
                                 "observed": np.average(block["observed"], weights=block["weight"]),
                                 "n": len(block)}), include_groups=False).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(6.5, 5))
    limit = max(calibration["predicted"].max(), calibration["observed"].max()) * 1.08
    ax.plot([0, limit], [0, limit], linestyle="--", color="#555", label="calibração ideal")
    ax.plot(calibration["predicted"], calibration["observed"], marker="o", color="#087e8b",
            label="teste interno por décimo")
    ax.set(xlabel="PHQ-8 modificado previsto", ylabel="PHQ-8 modificado observado",
           title="Calibração interna do modelo sem diagnóstico")
    ax.legend()
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIGURES / "prediction-calibration.png", dpi=180)
    plt.close(fig)

    def clean_model(model: dict) -> dict:
        return {key: value for key, value in model.items()
                if key not in {"beta", "covariance", "used_index"}}

    audit = {
        "H1_joined": len(h1), "H1_analyzed": m1["n"],
        "H2_joined": len(h2), "H2_analyzed": m2["n"],
        "H3_joined": len(h3), "H3_analyzed": m3["n"],
        "prediction_complete": len(prediction),
        "age_range": [int(prediction["RIDAGEYR"].min()), int(prediction["RIDAGEYR"].max())],
        "diagnostic_groups": "not_assessed",
    }
    hashes = {path.name: hashlib.sha256(path.read_bytes()).hexdigest()
              for path in sorted(DATA.glob("*.xpt")) if path.stem in
              {"DEMO_L", "DR1TOT_L", "DSQTOT_L", "SLQ_L", "PAQ_L", "DPQ_L"}}
    output = {"audit": audit, "models": {"H1": clean_model(m1), "H1_sensitivity": clean_model(m1_sensitivity),
              "H2": clean_model(m2), "H3": clean_model(m3)}, "primary_fdr": fdr,
              "prediction": metrics, "input_sha256": hashes}
    (OUT / "results.json").write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
