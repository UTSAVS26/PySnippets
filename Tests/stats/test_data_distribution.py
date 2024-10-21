import unittest
from pysnippets.stats.z_score_normalization import  z_score_normalization

class TestDataDistribution(unittest.TestCase):
    def test_z_score_normalization(self):
        self.assertAlmostEqual(z_score_normalization([1, 2, 3, 4, 5]), 
            [-1.4142135623730951, -0.7071067811865475, 0.0, 0.7071067811865475, 1.4142135623730951], 
            places=6)
        with self.assertRaises(ValueError):
            z_score_normalization([])

if __name__ == '__main__':
    unittest.main()
