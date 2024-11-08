import unittest
import pandas as pd
from feature_scaling import standardize_features, min_max_scale_features

class TestFeatureScaling(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Height': [150, 160, 170, 180],
            'Weight': [50, 60, 70, 80]
        })

    def test_standardize_features(self):
        scaled_df = standardize_features(self.df.copy(), ['Height', 'Weight'])
        self.assertAlmostEqual(scaled_df['Height'].mean(), 0.0, places=5)
        self.assertAlmostEqual(scaled_df['Weight'].mean(), 0.0, places=5)

    def test_min_max_scale_features(self):
        scaled_df = min_max_scale_features(self.df.copy(), ['Height', 'Weight'])
        self.assertEqual(scaled_df['Height'].min(), 0.0)
        self.assertEqual(scaled_df['Weight'].max(), 1.0)

if __name__ == '__main__':
    unittest.main() 