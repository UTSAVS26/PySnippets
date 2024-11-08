import unittest
import pandas as pd
from encoding import one_hot_encode, label_encode

class TestEncoding(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Color': ['Red', 'Blue', 'Green', 'Blue']
        })

    def test_one_hot_encode(self):
        encoded_df = one_hot_encode(self.df, 'Color')
        self.assertIn('Color_Green', encoded_df.columns)
        self.assertIn('Color_Red', encoded_df.columns)
        self.assertNotIn('Color', encoded_df.columns)

    def test_label_encode(self):
        encoded_df = label_encode(self.df.copy(), 'Color')
        self.assertTrue(encoded_df['Color'].dtype == int)
        self.assertEqual(encoded_df['Color'].min(), 0)

if __name__ == '__main__':
    unittest.main() 