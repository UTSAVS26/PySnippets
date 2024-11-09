import unittest
import numpy as np
from ML_snippets.decision_tree import DecisionTreeClassifier

class TestDecisionTreeClassifier(unittest.TestCase):
    def test_fit_predict(self):
        X = np.array([[2], [3], [10], [19]])
        y = np.array([0, 0, 1, 1])
        clf = DecisionTreeClassifier(max_depth=1)
        clf.fit(X, y)
        predictions = clf.predict(np.array([[4], [15]]))
        np.testing.assert_array_equal(predictions, np.array([0, 1]))

    def test_single_class(self):
        X = np.array([[1], [2], [3]])
        y = np.array([1, 1, 1])
        clf = DecisionTreeClassifier()
        clf.fit(X, y)
        predictions = clf.predict(np.array([[4], [5]]))
        np.testing.assert_array_equal(predictions, np.array([1, 1]))

if __name__ == '__main__':
    unittest.main() 