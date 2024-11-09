import unittest
import pandas as pd
from outlier_detection import remove_outliers_iqr, remove_outliers_zscore

class TestOutlierDetection(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Salary': [50000, 60000, 55000, 120000, 58000, 59000, 61000]
        })

    def test_remove_outliers_iqr(self):
        cleaned_df = remove_outliers_iqr(self.df, 'Salary')
        self.assertFalse((cleaned_df['Salary'] == 120000).any())

    def test_remove_outliers_zscore(self):
        cleaned_df = remove_outliers_zscore(self.df, 'Salary', threshold=2)
        self.assertFalse((cleaned_df['Salary'] == 120000).any())

if __name__ == '__main__':
    unittest.main() 