import unittest
import numpy as np
from ML_snippets.linear_regression import LinearRegressionModel

class TestLinearRegressionModel(unittest.TestCase):
    def test_fit_predict(self):
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])
        model = LinearRegressionModel()
        model.fit(X, y)
        predictions = model.predict(np.array([[6], [7]]))
        np.testing.assert_array_almost_equal(predictions, np.array([12., 14.]))

    def test_non_invertible_matrix(self):
        X = np.array([[1, 1], [1, 1], [1, 1]])
        y = np.array([2, 2, 2])
        model = LinearRegressionModel()
        with self.assertRaises(np.linalg.LinAlgError):
            model.fit(X, y)

if __name__ == '__main__':
    unittest.main() 