import unittest
import numpy as np
from ML_snippets.svm import SVM

class TestSVM(unittest.TestCase):
    def test_fit_predict(self):
        X = np.array([[2, 3], [1, 1], [2, 1], [3, 2]])
        y = np.array([1, -1, -1, 1])
        model = SVM(n_iters=1000)
        model.fit(X, y)
        predictions = model.predict(np.array([[3, 3], [1, 0]]))
        np.testing.assert_array_equal(predictions, np.array([1, -1]))

    def test_margin(self):
        X = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
        y = np.array([1, 1, 1, -1, -1])
        model = SVM(n_iters=1000)
        model.fit(X, y)
        predictions = model.predict(X)
        np.testing.assert_array_equal(predictions, y)

if __name__ == '__main__':
    unittest.main() 