import unittest
import pandas as pd
from feature_scaling import standardize_features, min_max_scale_features

class TestFeatureScaling(unittest.TestCase):
    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame({
            'Height': [150, 160, 170, 180],
            'Weight': [50, 60, 70, 80]
        })

    def test_standardize_features(self):
        # Test Standardization (mean should be 0 and std should be 1)
        scaled_df = standardize_features(self.df.copy(), ['Height', 'Weight'])
        self.assertAlmostEqual(scaled_df['Height'].mean(), 0.0, places=5, msg="Height column mean is not close to 0 after standardization.")
        self.assertAlmostEqual(scaled_df['Weight'].mean(), 0.0, places=5, msg="Weight column mean is not close to 0 after standardization.")
        self.assertAlmostEqual(scaled_df['Height'].std(), 1.0, places=5, msg="Height column standard deviation is not 1 after standardization.")
        self.assertAlmostEqual(scaled_df['Weight'].std(), 1.0, places=5, msg="Weight column standard deviation is not 1 after standardization.")

    def test_min_max_scale_features(self):
        # Test Min-Max Scaling (values should be in the range [0, 1])
        scaled_df = min_max_scale_features(self.df.copy(), ['Height', 'Weight'])
        self.assertEqual(scaled_df['Height'].min(), 0.0, "Min value of Height after Min-Max scaling should be 0.")
        self.assertEqual(scaled_df['Height'].max(), 1.0, "Max value of Height after Min-Max scaling should be 1.")
        self.assertEqual(scaled_df['Weight'].min(), 0.0, "Min value of Weight after Min-Max scaling should be 0.")
        self.assertEqual(scaled_df['Weight'].max(), 1.0, "Max value of Weight after Min-Max scaling should be 1.")

    def test_standardize_empty_df(self):
        # Test Standardization with an empty DataFrame
        empty_df = pd.DataFrame(columns=['Height', 'Weight'])
        scaled_df = standardize_features(empty_df, ['Height', 'Weight'])
        self.assertTrue(scaled_df.empty, "The scaled DataFrame should be empty for an empty input.")

    def test_min_max_scale_empty_df(self):
        # Test Min-Max Scaling with an empty DataFrame
        empty_df = pd.DataFrame(columns=['Height', 'Weight'])
        scaled_df = min_max_scale_features(empty_df, ['Height', 'Weight'])
        self.assertTrue(scaled_df.empty, "The scaled DataFrame should be empty for an empty input.")

    def test_standardize_single_value_column(self):
        # Test Standardization with a column that has only one unique value
        single_value_df = pd.DataFrame({'Height': [170, 170, 170, 170], 'Weight': [70, 70, 70, 70]})
        scaled_df = standardize_features(single_value_df, ['Height', 'Weight'])
        self.assertEqual(scaled_df['Height'].std(), 0.0, "The standard deviation of a single-value column should be 0.")
        self.assertEqual(scaled_df['Weight'].std(), 0.0, "The standard deviation of a single-value column should be 0.")
        self.assertEqual(scaled_df['Height'].mean(), 0.0, "The mean should be 0 for a column with a single unique value after standardization.")
        self.assertEqual(scaled_df['Weight'].mean(), 0.0, "The mean should be 0 for a column with a single unique value after standardization.")

    def test_min_max_scale_single_value_column(self):
        # Test Min-Max Scaling with a column that has only one unique value
        single_value_df = pd.DataFrame({'Height': [170, 170, 170, 170], 'Weight': [70, 70, 70, 70]})
        scaled_df = min_max_scale_features(single_value_df, ['Height', 'Weight'])
        self.assertEqual(scaled_df['Height'].min(), 0.0, "Min value should be 0 when there is only one unique value.")
        self.assertEqual(scaled_df['Height'].max(), 0.0, "Max value should be 0 when there is only one unique value.")
        self.assertEqual(scaled_df['Weight'].min(), 0.0, "Min value should be 0 when there is only one unique value.")
        self.assertEqual(scaled_df['Weight'].max(), 0.0, "Max value should be 0 when there is only one unique value.")

    def test_standardize_with_negative_values(self):
        # Test Standardization with negative values
        negative_df = pd.DataFrame({'Height': [-150, -160, -170, -180], 'Weight': [-50, -60, -70, -80]})
        scaled_df = standardize_features(negative_df, ['Height', 'Weight'])
        self.assertAlmostEqual(scaled_df['Height'].mean(), 0.0, places=5, msg="Mean of negative values after standardization should be 0.")
        self.assertAlmostEqual(scaled_df['Weight'].mean(), 0.0, places=5, msg="Mean of negative values after standardization should be 0.")

if __name__ == '__main__':
    unittest.main()
