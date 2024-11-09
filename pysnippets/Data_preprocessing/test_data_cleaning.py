import unittest
import pandas as pd
from data_cleaning import remove_duplicates, replace_missing_with_mean, standardize_text

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
            'Age': [25, 30, 25, None],
            'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
        })

    def test_remove_duplicates(self):
        cleaned_df = remove_duplicates(self.df)
        self.assertEqual(len(cleaned_df), 3)

    def test_replace_missing_with_mean(self):
        cleaned_df = replace_missing_with_mean(self.df, 'Age')
        self.assertEqual(cleaned_df.loc[3, 'Age'], 26.666666666666668)

    def test_standardize_text(self):
        standardized_df = standardize_text(self.df, 'Name')
        self.assertTrue(standardized_df['Name'].str.islower().all())

if __name__ == '__main__':
    unittest.main() 