import numpy as np
import unittest
from pysnippets.models.Ensemble import EnsembleModel  # Updated import

class TestEnsembleModel(unittest.TestCase):
    def setUp(self):
        self.model = EnsembleModel()
        self.X = np.random.rand(100, 2)
        self.y = (self.X[:, 0] + self.X[:, 1] > 1).astype(int)

    def test_fit_predict(self):
        self.model.fit(self.X, self.y)
        predictions = self.model.predict(self.X)
        self.assertEqual(predictions.shape, (100,))

    def test_score(self):
        self.model.fit(self.X, self.y)
        score = self.model.score(self.X, self.y)
        self.assertIsInstance(score, float)

if __name__ == '__main__':
    unittest.main()