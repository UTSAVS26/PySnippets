import numpy as np
import unittest
from pysnippets.models.Logistic_regression import LogisticModel  # Updated import

class TestLogisticModel(unittest.TestCase):
    def setUp(self):
        self.model = LogisticModel()
        self.X = np.random.rand(100, 2)
        self.y = (self.X[:, 0] + self.X[:, 1] > 1).astype(int)

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