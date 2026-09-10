"""Boundary checks for the cycle 004 analytic eligibility definition."""
import importlib.util
from pathlib import Path
import unittest

import pandas as pd


path = Path(__file__).resolve().parents[1] / "research/discoveries/cycle-004/run_analysis.py"
spec = importlib.util.spec_from_file_location("cycle004_analysis", path)
analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analysis)


class SelectionEligibilityTests(unittest.TestCase):
    def test_age_weight_and_design_boundaries(self):
        frame = pd.DataFrame({
            "RIDAGEYR": [19, 20, 80, 81, 40, 40],
            "WT": [1, 1, 1, 1, 0, 1],
            "SDMVSTRA": [1, 1, 1, 1, 1, None],
            "SDMVPSU": [1, 1, 1, 1, 1, 1],
            "SEX": [1, 1, 2, 2, 1, 1],
            "RACE": [1, 1, 2, 2, 1, 1],
        })
        eligible = analysis.eligible_domain(frame, pd.Series([True] * 6), "WT")
        self.assertEqual(eligible.tolist(), [False, True, True, False, False, False])


if __name__ == "__main__":
    unittest.main()
