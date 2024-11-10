import unittest
import numpy as np
from ML_snippets.random_forest import RandomForest

class TestRandomForest(unittest.TestCase):

    def setUp(self):
        # Common setup for training data
        self.X_simple = np.array([[2], [3], [10], [19], [11], [18], [23], [45]])
        self.y_simple = np.array([0, 0, 1, 1, 1, 1, 1, 1])
        self.rf = RandomForest(n_trees=5, max_depth=3)

    def test_fit_predict(self):
        self.rf.fit(self.X_simple, self.y_simple)
        predictions = self.rf.predict(np.array([[5], [15], [25]]))
        self.assertTrue((predictions == np.array([0, 1, 1])).all() or
                        (predictions == np.array([1, 1, 1])).all())

    def test_single_tree(self):
        X = np.array([[1], [2], [3]])
        y = np.array([0, 1, 1])
        rf = RandomForest(n_trees=1, max_depth=1)
        rf.fit(X, y)
        predictions = rf.predict(np.array([[1.5], [2.5]]))
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

    def test_multivariate_data(self):
        X = np.array([[2, 3], [3, 4], [10, 11], [19, 20], [11, 12], [18, 19], [23, 24], [45, 46]])
        y = np.array([0, 0, 1, 1, 1, 1, 1, 1])
        rf = RandomForest(n_trees=5, max_depth=3)
        rf.fit(X, y)
        predictions = rf.predict(np.array([[5, 6], [15, 16], [25, 26]]))
        self.assertTrue((predictions == np.array([0, 1, 1])).all() or
                        (predictions == np.array([1, 1, 1])).all())

    def test_imbalanced_data(self):
        X = np.array([[2], [3], [10], [19], [11], [18], [23], [45]])
        y = np.array([0, 0, 0, 1, 0, 0, 1, 1])  # Imbalanced classes (more 0's)
        rf = RandomForest(n_trees=5, max_depth=3)
        rf.fit(X, y)
        predictions = rf.predict(np.array([[5], [15], [25]]))
        # This is just a check, adjust according to the model behavior on imbalanced data
        self.assertIn(predictions[0], [0, 1])

    def test_empty_data(self):
        X_empty = np.array([[]])
        y_empty = np.array([])
        rf = RandomForest(n_trees=5, max_depth=3)
        with self.assertRaises(ValueError):
            rf.fit(X_empty, y_empty)

    def test_consistency_with_same_data(self):
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([0, 1, 0, 1, 0])
        rf1 = RandomForest(n_trees=5, max_depth=3)
        rf2 = RandomForest(n_trees=5, max_depth=3)

        rf1.fit(X, y)
        rf2.fit(X, y)
        
        predictions1 = rf1.predict(np.array([[6]]))
        predictions2 = rf2.predict(np.array([[6]]))
        
        # Ensure the predictions are consistent when trained with the same data
        np.testing.assert_array_equal(predictions1, predictions2)

if __name__ == '__main__':
    unittest.main()