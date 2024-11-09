import unittest
import pandas as pd
import numpy as np
from data_transformation import log_transform, power_transform, binarize

class TestDataTransformation(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Views': [100, 150, 200, 250, 300]
        })

    def test_log_transform(self):
        transformed_df = log_transform(self.df.copy(), 'Views')
        expected = np.log1p([100, 150, 200, 250, 300])
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected))

    def test_power_transform(self):
        transformed_df = power_transform(self.df.copy(), 'Views', power=2)
        expected = [100**2, 150**2, 200**2, 250**2, 300**2]
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected))

    def test_binarize(self):
        transformed_df = binarize(self.df.copy(), 'Views', threshold=200)
        expected = [0, 0, 1, 1, 1]
        pd.testing.assert_series_equal(transformed_df['Views'], pd.Series(expected))

if __name__ == '__main__':
    unittest.main() 