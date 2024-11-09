import unittest
import numpy as np
from ML_snippets.knearest_neighbors import KNearestNeighbors

class TestKNearestNeighbors(unittest.TestCase):
    def test_fit_predict(self):
        X_train = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 7], [8, 6]])
        y_train = np.array([0, 0, 0, 1, 1, 1])
        knn = KNearestNeighbors(k=3)
        knn.fit(X_train, y_train)
        predictions = knn.predict(np.array([[5, 5], [2, 2]]))
        np.testing.assert_array_equal(predictions, np.array([1, 0]))

    def test_k_equals_one(self):
        X_train = np.array([[0], [1], [2]])
        y_train = np.array([0, 1, 1])
        knn = KNearestNeighbors(k=1)
        knn.fit(X_train, y_train)
        predictions = knn.predict(np.array([[1.5]]))
        np.testing.assert_array_equal(predictions, np.array([1]))

if __name__ == '__main__':
    unittest.main() 