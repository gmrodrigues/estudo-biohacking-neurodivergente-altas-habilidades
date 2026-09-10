"""Regression checks for the magnesium measurement-state classification."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np
import pandas as pd


path = Path(__file__).resolve().parents[1] / "research/discoveries/cycle-003/run_audit.py"
spec = importlib.util.spec_from_file_location("cycle003_audit", path)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class MagnesiumStateTests(unittest.TestCase):
    def classify(self, total=np.nan, labelled=False, unmatched=False, records=np.nan):
        return audit.classify_magnesium_state(pd.Series({
            "DSQTMAGN": total,
            "any_label_magnesium": labelled,
            "any_no_or_unknown_match": unmatched,
            "reported_records": records,
        }))

    def test_quantified_value_takes_priority(self):
        self.assertEqual(self.classify(100.0, True, True, 2), "quantified_magnesium")

    def test_missing_total_states_remain_distinct(self):
        self.assertEqual(self.classify(labelled=True, records=1),
                         "magnesium_label_but_total_missing")
        self.assertEqual(self.classify(unmatched=True, records=1),
                         "no_magnesium_identified_with_unmatched_product")
        self.assertEqual(self.classify(records=1),
                         "reported_products_no_magnesium_identified")
        self.assertEqual(self.classify(), "no_released_product_record")


if __name__ == "__main__":
    unittest.main()
