"""Synthetic-only tests of coverage auditing and quiet failure."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import pandas as pd

from scripts.audit_analytic_export import audit, main


class AnalyticExportTests(unittest.TestCase):
    def setUp(self):
        self.config = {"source": "synthetic", "release": "test",
                       "mapping_status": "reviewed", "missing_values": [""],
                       "keys": ["id", "event"],
                       "roles": {"capacity": ["c"], "exposure": ["x"],
                                 "outcome": ["y"], "context": ["age"],
                                 "condition": ["d"]},
                       "event_pair": ["baseline", "followup"]}
        self.frame = pd.DataFrame([
            ["001", "baseline", 10, 2, 5, 9, 1],
            ["001", "followup", None, None, 6, 11, None],
            ["002", "baseline", 12, None, 7, 9, 0]],
            columns=["id", "event", "c", "x", "y", "age", "d"])

    def test_counts_joint_coverage_without_requiring_followup_exposure(self):
        r = audit(self.frame, self.config)
        self.assertEqual(r["participants"], 2)
        self.assertEqual(r["core_complete_rows"], 1)
        self.assertEqual(r["longitudinal_complete_pairs"], 1)
        self.assertEqual(r["status"], "coverage_only_not_poc_approved")

    def test_duplicate_keys_and_circular_roles_rejected(self):
        with self.assertRaises(ValueError):
            audit(pd.concat([self.frame, self.frame.iloc[:1]]), self.config)
        self.config["roles"]["capacity"] = ["y"]
        with self.assertRaises(ValueError):
            audit(self.frame, self.config)

    def test_failure_does_not_echo_value_or_write_report(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.frame["c"] = self.frame["c"].astype(object)
            self.frame.loc[0, "c"] = "PRIVATE_SENTINEL"
            self.frame.to_csv(root / "input.csv", index=False)
            (root / "config.json").write_text(json.dumps(self.config))
            output = io.StringIO()
            with patch("sys.argv", ["audit", "--input", str(root / "input.csv"),
                                  "--config", str(root / "config.json"),
                                  "--output", str(root / "report.json")]):
                with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                    self.assertEqual(main(), 1)
            self.assertNotIn("PRIVATE_SENTINEL", output.getvalue())
            self.assertFalse((root / "report.json").exists())

    def test_cli_preserves_ids_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.frame.to_csv(root / "input.csv", index=False)
            (root / "config.json").write_text(json.dumps(self.config))
            with patch("sys.argv", ["audit", "--input", str(root / "input.csv"),
                                  "--config", str(root / "config.json"),
                                  "--output", str(root / "report.json")]):
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(main(), 0)
                    original = (root / "report.json").read_bytes()
                    self.assertEqual(main(), 1)
            self.assertEqual(original, (root / "report.json").read_bytes())
            self.assertEqual(json.loads(original)["longitudinal_complete_pairs"], 1)


if __name__ == "__main__":
    unittest.main()
