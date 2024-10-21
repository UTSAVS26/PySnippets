import numpy as np
import unittest
from pysnippets.models.KMeans import KMeansModel  # Updated import

class TestKMeansModel(unittest.TestCase):
    def setUp(self):
        self.model = KMeansModel(n_clusters=3)
        self.X = np.random.rand(100, 2)

    def test_fit_predict(self):
        self.model.fit(self.X)
        predictions = self.model.predict(self.X)
        self.assertEqual(predictions.shape, (100,))

if __name__ == '__main__':
    unittest.main()