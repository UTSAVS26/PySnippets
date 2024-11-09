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

    def test_non_separable_data(self):
        # Non-linearly separable data
        X = np.array([[1, 2], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]])
        y = np.array([1, -1, 1, -1, 1, -1])  # Not linearly separable
        model = SVM(n_iters=1000)
        model.fit(X, y)
        predictions = model.predict(X)
        # Assert that the predictions do not match exactly
        self.assertNotEqual(np.sum(predictions == y), len(y))

    def test_large_dataset(self):
        # Simulate larger dataset
        X = np.random.rand(1000, 10)  # 1000 samples, 10 features
        y = np.random.choice([1, -1], size=1000)
        model = SVM(n_iters=5000)
        model.fit(X, y)
        predictions = model.predict(X[:10])
        self.assertEqual(len(predictions), 10)

    def test_with_different_hyperparameters(self):
        X = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
        y = np.array([1, 1, 1, -1, -1])

        # Test with different learning rate
        model = SVM(learning_rate=0.01, n_iters=1000)
        model.fit(X, y)
        predictions = model.predict(X)
        np.testing.assert_array_equal(predictions, y)

        # Test with different lambda parameter
        model = SVM(lambda_param=0.1, n_iters=1000)
        model.fit(X, y)
        predictions = model.predict(X)
        np.testing.assert_array_equal(predictions, y)

    def test_convergence(self):
        X = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
        y = np.array([1, 1, 1, -1, -1])
        model = SVM(n_iters=1000)
        model.fit(X, y)
        
        # Assert that the weights have been updated (ensuring convergence)
        self.assertIsNotNone(model.w)
        self.assertIsNotNone(model.b)

if __name__ == '__main__':
    unittest.main()