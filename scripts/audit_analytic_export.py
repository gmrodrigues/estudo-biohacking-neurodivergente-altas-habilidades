"""Audit a locally authorized, harmonized CSV without sending rows to stdout.

Input must already use codebook-approved missing values and one row per person/event.
This checks structural coverage, not scientific validity or causal identification.
"""
import argparse
import json
import os
from pathlib import Path
import sys

import pandas as pd


def audit(frame, config):
    keys = config["keys"]
    roles = config["roles"]
    required_roles = ("capacity", "exposure", "outcome", "context")
    if len(keys) != 2 or len(set(keys)) != 2:
        raise ValueError("keys")
    if any(not roles.get(role) for role in required_roles):
        raise ValueError("roles")
    flat = [c for values in roles.values() for c in values]
    if len(flat) != len(set(flat)) or set(keys).intersection(flat):
        raise ValueError("overlapping_roles")
    required = keys + flat
    if any(c not in frame for c in required):
        raise ValueError("columns")
    if frame[keys].isna().any().any() or frame.duplicated(keys).any():
        raise ValueError("keys")
    # IDs are strings on CLI ingestion: never coerce leading zeros away.
    numeric = frame.copy()
    for column in flat:
        numeric[column] = pd.to_numeric(numeric[column], errors="raise")
        present = numeric[column].dropna()
        if not present.map(lambda x: float("-inf") < x < float("inf")).all():
            raise ValueError("nonfinite")
    masks = {role: numeric[columns].notna().all(axis=1)
             for role, columns in roles.items()}
    core = masks["capacity"] & masks["exposure"] & masks["outcome"] & masks["context"]
    conditions = masks.get("condition", pd.Series(False, index=frame.index))
    result = {
        "status": "coverage_only_not_poc_approved",
        "source": config["source"],
        "release": config["release"],
        "rows": len(frame),
        "participants": int(frame[keys[0]].nunique()),
        "complete_rows_by_role": {r: int(m.sum()) for r, m in masks.items()},
        "core_complete_rows": int(core.sum()),
        "core_complete_participants": int(frame.loc[core, keys[0]].nunique()),
        "core_with_condition_rows": int((core & conditions).sum()),
        "longitudinal_complete_pairs": None,
        "limits": ["No psychometric validation, power assessment, or effect estimation.",
                   "No condition prevalence or high-capacity threshold inferred.",
                   "Missing-code normalization and instrument mapping require prior review."]
    }
    events = config.get("event_pair")
    if events:
        if len(events) != 2 or events[0] == events[1]:
            raise ValueError("events")
        # Require baseline and follow-up outcome, preserving the baseline adjustment.
        baseline_ids = set(frame.loc[core & frame[keys[1]].eq(events[0]), keys[0]])
        later_ids = set(frame.loc[masks["outcome"] & frame[keys[1]].eq(events[1]), keys[0]])
        result["longitudinal_complete_pairs"] = len(baseline_ids & later_ids)
        result["limits"].append("Event order supplied by configuration; dates/windows not validated.")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        config = json.loads(args.config.read_text())
        if config.get("mapping_status") != "reviewed":
            raise ValueError("unreviewed_mapping")
        frame = pd.read_csv(args.input, dtype="string", keep_default_na=False,
                            na_values=config["missing_values"])
        report = audit(frame, config)
        # Exclusive creation protects inputs and prior reports; mode is owner-only.
        fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w") as stream:
            json.dump(report, stream, indent=2)
            stream.write("\n")
    except Exception:
        # Parser exceptions can contain participant values; never echo exception text.
        print("Audit failed; verify mapping, keys, numeric values and output path locally.",
              file=sys.stderr)
        return 1
    print("Audit completed; report saved locally. No records returned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
