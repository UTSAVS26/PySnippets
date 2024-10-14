# test_quantile.py

import unittest
from pysnippets.stats.quantile import quantile

class TestDataDistribution(unittest.TestCase):

    def test_quantile(self):
        # Basic test cases
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0.5), 3)
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0.25), 2)
        
        # Edge cases
        self.assertEqual(quantile([1, 2, 3, 4, 5], 0), 1)
        self.assertEqual(quantile([1, 2, 3, 4, 5], 1), 5)
        
        # Test with repeated elements
        self.assertEqual(quantile([1, 1, 1, 1, 1], 0.5), 1)
        
        # Test with negative numbers
        self.assertEqual(quantile([-5, -1, -3, -2, -4], 0.5), -3)
        
        # Test with floating point numbers
        self.assertAlmostEqual(quantile([1.1, 2.2, 3.3, 4.4, 5.5], 0.5), 3.3)
        
        # Test with empty list
        with self.assertRaises(ValueError):
            quantile([], 0.5)
        
        # Test with invalid quantile
        with self.assertRaises(ValueError):
            quantile([1, 2, 3, 4, 5], 1.5)
        with self.assertRaises(ValueError):
            quantile([1, 2, 3, 4, 5], -0.5)

        # Test with non-numeric values
        with self.assertRaises(ValueError):
            quantile([1, 2, 'three', 4, 5], 0.5)

if __name__ == '__main__':
    unittest.main()
