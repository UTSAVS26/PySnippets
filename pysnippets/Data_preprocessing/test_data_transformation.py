import unittest
import pandas as pd
import numpy as np
from data_transformation import log_transform, power_transform, binarize

class TestDataTransformation(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame({
            'Views': [100, 150, 200, 250, 300]
        })

    def test_log_transform(self):
        # Test Log Transformation (log1p applied)
        transformed_df = log_transform(self.df.copy(), 'Views')
        expected = np.log1p([100, 150, 200, 250, 300])
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_power_transform(self):
        # Test Power Transformation (square by default)
        transformed_df = power_transform(self.df.copy(), 'Views', power=2)
        expected = [100**2, 150**2, 200**2, 250**2, 300**2]
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_binarize(self):
        # Test Binarization (threshold at 200)
        transformed_df = binarize(self.df.copy(), 'Views', threshold=200)
        expected = [0, 0, 1, 1, 1]
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_log_transform_edge_case(self):
        # Test Log Transformation with 0 (should handle log(0) = -inf gracefully)
        df_zero = pd.DataFrame({'Views': [0, 1, 2]})
        transformed_df = log_transform(df_zero, 'Views')
        expected = np.log1p([0, 1, 2])
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_power_transform_negative_power(self):
        # Test Power Transformation with negative power (should work with fractional values)
        transformed_df = power_transform(self.df.copy(), 'Views', power=-2)
        expected = [100**-2, 150**-2, 200**-2, 250**-2, 300**-2]
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_binarize_edge_case(self):
        # Test Binarization with threshold lower than all values
        transformed_df = binarize(self.df.copy(), 'Views', threshold=50)
        expected = [1, 1, 1, 1, 1]  # All values should be 1 since threshold is 50
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected), check_dtype=False)

    def test_empty_dataframe(self):
        # Test transformations on an empty DataFrame
        empty_df = pd.DataFrame({'Views': []})
        transformed_df = log_transform(empty_df, 'Views')
        self.assertTrue(transformed_df.empty, "The transformed DataFrame should be empty.")

        transformed_df = power_transform(empty_df, 'Views', power=2)
        self.assertTrue(transformed_df.empty, "The transformed DataFrame should be empty.")

        transformed_df = binarize(empty_df, 'Views', threshold=200)
        self.assertTrue(transformed_df.empty, "The transformed DataFrame should be empty.")

    def test_binarize_non_numeric(self):
        # Test Binarization on a non-numeric column (should raise error)
        df_non_numeric = pd.DataFrame({'Views': ['a', 'b', 'c', 'd', 'e']})
        with self.assertRaises(TypeError):
            binarize(df_non_numeric, 'Views', threshold=200)

if __name__ == '__main__':
    unittest.main()
