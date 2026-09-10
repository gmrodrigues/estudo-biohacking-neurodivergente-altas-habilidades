"""Analytic fixture: a domain empties one PSU but must preserve its variance."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np
import pandas as pd

path = Path(__file__).resolve().parents[1] / 'research/discoveries/cycle-002/run_audit.py'
spec = importlib.util.spec_from_file_location('cycle002_audit', path)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class FullDesignAuditTests(unittest.TestCase):
    def test_empty_domain_psu_still_contributes_to_variance(self):
        frame = pd.DataFrame({
            'SEQN': range(8), 'SDMVSTRA': [1]*4 + [2]*4,
            'SDMVPSU': [1, 1, 2, 2]*2, 'weight': [1.]*8,
            'response': [1., 3., 99., 99., 5., 7., 9., 11.],
        })
        domain = pd.Series([True, True, False, False, True, True, True, True])
        # Mean = 6. PSU influence sums: (-8/6, 0), (0, 8/6).
        # With two PSUs per stratum, variance = sum squared pair differences.
        expected_se = np.sqrt(32/9)
        reference = {'df_design': 2, 'coefficients': {
            'Intercept': {'estimate': 6., 'se': expected_se, 'p_value': 0.},
        }}
        result = audit.compare_svy(frame, domain, 'response ~ 1', 'weight', reference)
        self.assertEqual(result['full_design_n'], 8)
        self.assertAlmostEqual(result['terms'][0]['svy_estimate'], 6., places=10)
        self.assertAlmostEqual(result['terms'][0]['svy_se'], expected_se, places=10)


if __name__ == '__main__':
    unittest.main()
