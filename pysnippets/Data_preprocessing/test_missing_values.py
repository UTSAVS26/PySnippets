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

    def test_impute_numeric_with_mean_all_missing(self):
        # All values are missing in the column 'Income', check imputation with mean.
        df_all_missing = pd.DataFrame({
            'Age': [25, np.nan, 30, 22],
            'Gender': ['M', 'F', np.nan, 'F'],
            'Income': [np.nan, np.nan, np.nan, np.nan]
        })
        imputed_df = impute_numeric_with_mean(df_all_missing, ['Income'])
        self.assertAlmostEqual(imputed_df['Income'].iloc[0], np.nan)

    def test_drop_missing_empty_df(self):
        # Test for an empty DataFrame
        empty_df = pd.DataFrame(columns=['Age', 'Gender', 'Income'])
        cleaned_df = drop_missing(empty_df, threshold=0.5)
        self.assertTrue(cleaned_df.empty, "Empty DataFrame should remain empty.")

    def test_impute_categorical_with_mode_empty(self):
        # Test impute categorical with mode for empty column 'Gender'
        df_empty_cat = pd.DataFrame({
            'Age': [25, np.nan, 30, 22],
            'Gender': [np.nan, np.nan, np.nan, np.nan],
            'Income': [50000, 60000, np.nan, 52000]
        })
        imputed_df = impute_categorical_with_mode(df_empty_cat, ['Gender'])
        self.assertEqual(imputed_df['Gender'].isna().sum(), 0)

    def test_drop_missing_threshold_1(self):
        # Test with a threshold of 1 (i.e., drop rows with any missing values)
        df_with_missing = pd.DataFrame({
            'Age': [25, np.nan, 30, 22],
            'Gender': ['M', 'F', np.nan, 'F'],
            'Income': [50000, 60000, np.nan, 52000]
        })
        cleaned_df = drop_missing(df_with_missing, threshold=1)
        self.assertEqual(len(cleaned_df), 0, "All rows should be dropped when threshold is 1.0.")

    def test_drop_missing_no_missing(self):
        # Test for no missing values in the DataFrame
        df_no_missing = pd.DataFrame({
            'Age': [25, 30, 30, 22],
            'Gender': ['M', 'F', 'M', 'F'],
            'Income': [50000, 60000, 65000, 52000]
        })
        cleaned_df = drop_missing(df_no_missing, threshold=0.67)
        self.assertEqual(len(cleaned_df), 4, "No rows should be dropped when there are no missing values.")

if __name__ == '__main__':
    unittest.main()
