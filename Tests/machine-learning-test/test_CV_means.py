import numpy as np
import unittest
from pysnippets.models.CV_means import CVMeansModel  # Updated import

class TestCVMeansModel(unittest.TestCase):
    def setUp(self):
        self.model = CVMeansModel()
        self.X = np.random.rand(100, 10)
        self.y = np.random.rand(100)

    def test_cross_val_mean(self):
        mean_score = self.model.cross_val_mean(self.X, self.y)
        self.assertIsInstance(mean_score, float)

if __name__ == '__main__':
    unittest.main()