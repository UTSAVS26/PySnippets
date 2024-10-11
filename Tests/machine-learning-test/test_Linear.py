import numpy as np
import unittest
from pysnippets.models.Linear_regression import LinearModel  # Updated import

class TestLinearModel(unittest.TestCase):
    def setUp(self):
        self.model = LinearModel()
        self.X = np.random.rand(100, 1)
        self.y = 2 * self.X + np.random.rand(100, 1)

    def test_fit_predict(self):
        self.model.fit(self.X, self.y)
        predictions = self.model.predict(self.X)
        self.assertEqual(predictions.shape, self.y.shape)

    def test_score(self):
        self.model.fit(self.X, self.y)
        score = self.model.score(self.X, self.y)
        self.assertIsInstance(score, float)

if __name__ == '__main__':
    unittest.main()