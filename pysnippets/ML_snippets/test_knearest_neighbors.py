import unittest
import numpy as np
from ML_snippets.knearest_neighbors import KNearestNeighbors

class TestKNearestNeighbors(unittest.TestCase):
    
    def setUp(self):
        # Setup common training data
        self.X_train = np.array([[1, 2], [2, 3], [3, 3], [6, 5], [7, 7], [8, 6]])
        self.y_train = np.array([0, 0, 0, 1, 1, 1])
    
    def test_fit_predict_k3(self):
        knn = KNearestNeighbors(k=3)
        knn.fit(self.X_train, self.y_train)
        predictions = knn.predict(np.array([[5, 5], [2, 2]]))
        np.testing.assert_array_equal(predictions, np.array([1, 0]))

    def test_k_equals_one(self):
        knn = KNearestNeighbors(k=1)
        knn.fit(self.X_train, self.y_train)
        predictions = knn.predict(np.array([[1.5]]))
        np.testing.assert_array_equal(predictions, np.array([1]))

    def test_k_equals_large_value(self):
        knn = KNearestNeighbors(k=10)  # k greater than the number of samples
        knn.fit(self.X_train, self.y_train)
        predictions = knn.predict(np.array([[1, 1], [6, 6]]))
        # Expect predictions based on majority voting, considering all samples
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

    def test_predict_multiple_classes(self):
        X_train = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
        y_train = np.array([0, 0, 1, 1, 2])
        knn = KNearestNeighbors(k=3)
        knn.fit(X_train, y_train)
        predictions = knn.predict(np.array([[2.5, 2.5], [3.5, 3.5]]))
        # The first sample is closer to [2, 2] and [3, 3] (class 0 and 1), while the second is closer to [4, 4] and [5, 5] (class 1)
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

    def test_edge_case_all_same_label(self):
        X_train = np.array([[1, 2], [2, 3], [3, 3]])
        y_train = np.array([1, 1, 1])  # All the same label
        knn = KNearestNeighbors(k=2)
        knn.fit(X_train, y_train)
        predictions = knn.predict(np.array([[1, 1]]))
        np.testing.assert_array_equal(predictions, np.array([1]))

    def test_invalid_k(self):
        knn = KNearestNeighbors(k=10)
        knn.fit(self.X_train, self.y_train)
        # k is larger than the number of samples, so it should predict based on all points
        predictions = knn.predict(np.array([[1, 1], [5, 5]]))
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

if __name__ == '__main__':
    unittest.main()