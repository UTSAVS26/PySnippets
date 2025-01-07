import unittest
import pandas as pd
from encoding import one_hot_encode, label_encode

class TestEncoding(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame({
            'Color': ['Red', 'Blue', 'Green', 'Blue']
        })

    def test_one_hot_encode(self):
        # Test One-Hot Encoding
        encoded_df = one_hot_encode(self.df, 'Color')
        self.assertIn('Color_Green', encoded_df.columns, "Encoded DataFrame should contain 'Color_Green'.")
        self.assertIn('Color_Red', encoded_df.columns, "Encoded DataFrame should contain 'Color_Red'.")
        self.assertNotIn('Color', encoded_df.columns, "Original 'Color' column should be dropped.")
        self.assertEqual(encoded_df.shape[1], 3, "The number of columns after one-hot encoding is incorrect.")

    def test_label_encode(self):
        # Test Label Encoding
        encoded_df = label_encode(self.df.copy(), 'Color')
        self.assertTrue(encoded_df['Color'].dtype == int, "Encoded column should have integer dtype.")
        self.assertEqual(encoded_df['Color'].min(), 0, "The minimum label value should be 0.")
        self.assertEqual(encoded_df['Color'].max(), 2, "The maximum label value should be 2 (for 'Red', 'Blue', 'Green').")
        
    def test_one_hot_encode_empty_df(self):
        # Test One-Hot Encoding with an empty DataFrame
        empty_df = pd.DataFrame(columns=['Color'])
        encoded_df = one_hot_encode(empty_df, 'Color')
        self.assertTrue(encoded_df.empty, "The encoded DataFrame should be empty when the input is empty.")

    def test_label_encode_empty_df(self):
        # Test Label Encoding with an empty DataFrame
        empty_df = pd.DataFrame(columns=['Color'])
        encoded_df = label_encode(empty_df, 'Color')
        self.assertTrue(encoded_df.empty, "The encoded DataFrame should be empty when the input is empty.")
    
    def test_one_hot_encode_single_unique_value(self):
        # Test One-Hot Encoding when there is only one unique value in the column
        single_value_df = pd.DataFrame({'Color': ['Red', 'Red', 'Red', 'Red']})
        encoded_df = one_hot_encode(single_value_df, 'Color')
        self.assertIn('Color_Red', encoded_df.columns, "Encoded DataFrame should contain 'Color_Red'.")
        self.assertEqual(encoded_df.shape[1], 1, "The number of columns after one-hot encoding with a single value should be 1.")
    
    def test_label_encode_single_unique_value(self):
        # Test Label Encoding when there is only one unique value in the column
        single_value_df = pd.DataFrame({'Color': ['Red', 'Red', 'Red', 'Red']})
        encoded_df = label_encode(single_value_df, 'Color')
        self.assertEqual(encoded_df['Color'].min(), 0, "The encoded value should be 0 for a single unique value.")
        self.assertEqual(encoded_df['Color'].max(), 0, "The encoded value should be 0 for a single unique value.")

    def test_label_encode_non_string_column(self):
        # Test Label Encoding with a non-string column (e.g., numeric)
        numeric_df = pd.DataFrame({'Color': [1, 2, 1, 3]})
        encoded_df = label_encode(numeric_df, 'Color')
        self.assertTrue(encoded_df['Color'].dtype == int, "Encoded column should have integer dtype.")
        self.assertEqual(encoded_df['Color'].min(), 0, "The minimum label value should be 0.")

if __name__ == '__main__':
    unittest.main()
