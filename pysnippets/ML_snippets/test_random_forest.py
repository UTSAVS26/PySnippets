import unittest
import numpy as np
from ML_snippets.random_forest import RandomForest

class TestRandomForest(unittest.TestCase):
    def test_fit_predict(self):
        X = np.array([[2], [3], [10], [19], [11], [18], [23], [45]])
        y = np.array([0, 0, 1, 1, 1, 1, 1, 1])
        rf = RandomForest(n_trees=5, max_depth=3)
        rf.fit(X, y)
        predictions = rf.predict(np.array([[5], [15], [25]]))
        self.assertTrue((predictions == np.array([0, 1, 1])).all() or
                        (predictions == np.array([1, 1, 1])).all())

    def test_single_tree(self):
        X = np.array([[1], [2], [3]])
        y = np.array([0, 1, 1])
        rf = RandomForest(n_trees=1, max_depth=1)
        rf.fit(X, y)
        predictions = rf.predict(np.array([[1.5], [2.5]]))
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

if __name__ == '__main__':
    unittest.main() 