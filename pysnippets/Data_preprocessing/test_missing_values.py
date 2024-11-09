import unittest
import pandas as pd
import numpy as np
from missing_values import impute_numeric_with_mean, impute_categorical_with_mode, drop_missing

class TestMissingValues(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Age': [25, np.nan, 30, 22],
            'Gender': ['M', 'F', np.nan, 'F'],
            'Income': [50000, 60000, np.nan, 52000]
        })

    def test_impute_numeric_with_mean(self):
        imputed_df = impute_numeric_with_mean(self.df.copy(), ['Age', 'Income'])
        self.assertAlmostEqual(imputed_df.loc[1, 'Age'], 25.666666666666668)
        self.assertAlmostEqual(imputed_df.loc[2, 'Income'], 54000.0)

    def test_impute_categorical_with_mode(self):
        imputed_df = impute_categorical_with_mode(self.df.copy(), ['Gender'])
        self.assertEqual(imputed_df.loc[2, 'Gender'], 'F')

    def test_drop_missing(self):
        cleaned_df = drop_missing(self.df.copy(), threshold=0.67)
        self.assertEqual(len(cleaned_df), 3)

if __name__ == '__main__':
    unittest.main() 