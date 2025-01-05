import unittest
import pandas as pd
from data_cleaning import remove_duplicates, replace_missing_with_mean, standardize_text

class TestDataCleaning(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame({
            'Name': ['Alice', 'Bob', 'Alice', 'Charlie'],
            'Age': [25, 30, 25, None],
            'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
        })

    def test_remove_duplicates(self):
        # Test that duplicates are removed
        cleaned_df = remove_duplicates(self.df)
        self.assertEqual(len(cleaned_df), 3, "Duplicates were not removed correctly.")
        self.assertTrue('Alice' in cleaned_df['Name'].values, "Duplicate for 'Alice' was not removed.")

    def test_replace_missing_with_mean(self):
        # Test replacing missing values with the mean
        cleaned_df = replace_missing_with_mean(self.df, 'Age')
        expected_mean = self.df['Age'].mean()
        self.assertEqual(cleaned_df.loc[3, 'Age'], expected_mean, "Missing value was not replaced correctly with the mean.")
        
    def test_standardize_text(self):
        # Test standardizing text (lowercase and stripped)
        standardized_df = standardize_text(self.df, 'Name')
        self.assertTrue(standardized_df['Name'].str.islower().all(), "Text was not standardized to lowercase.")
        self.assertFalse(standardized_df['Name'].str.contains(' ').any(), "Text was not stripped of whitespace.")

    def test_replace_missing_with_mean_no_missing_values(self):
        # Test replacing missing values when there are no missing values
        df_no_missing = self.df.copy()
        df_no_missing['Age'].iloc[3] = 29  # No missing value in 'Age'
        cleaned_df = replace_missing_with_mean(df_no_missing, 'Age')
        self.assertEqual(cleaned_df.loc[3, 'Age'], 29, "The value should remain unchanged when there is no missing value.")

    def test_remove_duplicates_empty_df(self):
        # Test that no error is raised when removing duplicates from an empty DataFrame
        empty_df = pd.DataFrame(columns=self.df.columns)
        cleaned_df = remove_duplicates(empty_df)
        self.assertEqual(len(cleaned_df), 0, "Removing duplicates from an empty DataFrame failed.")

    def test_standardize_text_empty_column(self):
        # Test standardizing text for an empty column
        empty_df = pd.DataFrame({'Name': []})
        cleaned_df = standardize_text(empty_df, 'Name')
        self.assertEqual(len(cleaned_df), 0, "Standardizing text on an empty column failed.")

if __name__ == '__main__':
    unittest.main()
