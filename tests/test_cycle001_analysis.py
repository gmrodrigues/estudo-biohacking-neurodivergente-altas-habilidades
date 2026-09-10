"""Regression checks for the documented H2 boundary error and multiplicity."""

import importlib.util
from pathlib import Path
import unittest

import numpy as np
import pandas as pd
from statsmodels.stats.multitest import multipletests


path = Path(__file__).resolve().parents[1] / "research/discoveries/cycle-001/run_analysis.py"
spec = importlib.util.spec_from_file_location("cycle001_analysis", path)
analysis = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analysis)


class AnalysisRegressionTests(unittest.TestCase):
    def test_registered_sleep_boundaries_and_missing(self):
        hours = pd.Series([2, 6.5, 7, 7.5, 9, 9.5, 14, np.nan], index=range(11, 19))
        groups = analysis.sleep_categories(hours)
        self.assertEqual(groups.iloc[:7].tolist(),
                         ["short", "short", "recommended", "recommended",
                          "recommended", "long", "long"])
        self.assertTrue(pd.isna(groups.iloc[7]))
        self.assertTrue(groups.index.equals(hours.index))
        self.assertEqual(groups.cat.categories[0], "recommended")

    def test_eight_term_fdr_matches_independent_implementation(self):
        # Unsorted values with ties exercise ordering, monotonicity and clipping.
        p_values = dict(zip("abcdefgh", [0.99, 0.04, 0.001, 0.04, 0.2, 0.008, 1, 0.4]))
        actual = analysis.bh_fdr(p_values)
        expected = multipletests(list(p_values.values()), method="fdr_bh")[1]
        np.testing.assert_allclose([actual[key] for key in p_values], expected)


if __name__ == "__main__":
    unittest.main()
