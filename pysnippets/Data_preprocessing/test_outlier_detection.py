import unittest
import pandas as pd
from outlier_detection import remove_outliers_iqr, remove_outliers_zscore

class TestOutlierDetection(unittest.TestCase):
    def setUp(self):
        # A sample DataFrame with salary data, including an outlier (120000)
        self.df = pd.DataFrame({
            'Salary': [50000, 60000, 55000, 120000, 58000, 59000, 61000]
        })

    def test_remove_outliers_iqr(self):
        # Remove outliers using IQR method
        cleaned_df = remove_outliers_iqr(self.df, 'Salary')
        
        # Ensure that the outlier (120000) is removed
        self.assertFalse((cleaned_df['Salary'] == 120000).any())
        
        # Check if the length of the DataFrame is reduced by one (1 outlier should be removed)
        self.assertEqual(len(cleaned_df), len(self.df) - 1, "One row should be removed when outlier is detected.")

    def test_remove_outliers_zscore(self):
        # Remove outliers using Z-score method (with a threshold of 2)
        cleaned_df = remove_outliers_zscore(self.df, 'Salary', threshold=2)
        
        # Ensure that the outlier (120000) is removed
        self.assertFalse((cleaned_df['Salary'] == 120000).any())
        
        # Check if the length of the DataFrame is reduced by one (1 outlier should be removed)
        self.assertEqual(len(cleaned_df), len(self.df) - 1, "One row should be removed when outlier is detected.")

    def test_no_outliers(self):
        # A DataFrame with no outliers
        df_no_outliers = pd.DataFrame({
            'Salary': [50000, 60000, 55000, 58000, 59000, 61000]
        })
        
        # Check if the length remains the same
        cleaned_df = remove_outliers_iqr(df_no_outliers, 'Salary')
        self.assertEqual(len(cleaned_df), len(df_no_outliers), "No rows should be removed if there are no outliers.")
        
        # Also test using Z-score method with a threshold of 2
        cleaned_df = remove_outliers_zscore(df_no_outliers, 'Salary', threshold=2)
        self.assertEqual(len(cleaned_df), len(df_no_outliers), "No rows should be removed if there are no outliers.")

    def test_multiple_outliers(self):
        # Data with multiple outliers
        df_multiple_outliers = pd.DataFrame({
            'Salary': [50000, 60000, 55000, 120000, 130000, 140000, 61000]
        })
        
        # Remove outliers using IQR method
        cleaned_df = remove_outliers_iqr(df_multiple_outliers, 'Salary')
        self.assertNotIn(120000, cleaned_df['Salary'].values)
        self.assertNotIn(130000, cleaned_df['Salary'].values)
        self.assertNotIn(140000, cleaned_df['Salary'].values)
        self.assertEqual(len(cleaned_df), len(df_multiple_outliers) - 3, "Three outliers should be removed.")
        
        # Remove outliers using Z-score method
        cleaned_df = remove_outliers_zscore(df_multiple_outliers, 'Salary', threshold=2)
        self.assertNotIn(120000, cleaned_df['Salary'].values)
        self.assertNotIn(130000, cleaned_df['Salary'].values)
        self.assertNotIn(140000, cleaned_df['Salary'].values)
        self.assertEqual(len(cleaned_df), len(df_multiple_outliers) - 3, "Three outliers should be removed.")

if __name__ == '__main__':
    unittest.main()
