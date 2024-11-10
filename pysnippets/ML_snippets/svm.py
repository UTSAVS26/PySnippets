import numpy as np

class SVM:
    """
    Support Vector Machine (SVM) classifier using a linear kernel.

    Parameters:
    -----------
    learning_rate : float
        Learning rate for gradient descent.
    lambda_param : float
        Regularization parameter.
    n_iters : int
        Number of iterations for training.
    """

    def __init__(self, learning_rate: float = 0.001, lambda_param: float = 0.01, n_iters: int = 1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Train the SVM model using gradient descent.

        Parameters:
        -----------
        X : np.ndarray
            Training data, shape (n_samples, n_features).
        y : np.ndarray
            Target labels, shape (n_samples,).
        """
        y_ = np.where(y <= 0, -1, 1)  # Convert labels to -1, 1
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features)
        self.b = 0

        for _ in range(self.n_iters):
            # Shuffle data for each iteration to prevent bias
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y_[indices]

            # Gradient descent
            for idx, x_i in enumerate(X_shuffled):
                condition = y_shuffled[idx] * (np.dot(x_i, self.w) - self.b) >= 1
                if condition:
                    self.w -= self.lr * (2 * self.lambda_param * self.w)  # Regularization term
                else:
                    self.w -= self.lr * (2 * self.lambda_param * self.w - np.dot(x_i, y_shuffled[idx]))
                    self.b -= self.lr * y_shuffled[idx]

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for the input data.

        Parameters:
        -----------
        X : np.ndarray
            Input data, shape (n_samples, n_features).
        
        Returns:
        --------
        np.ndarray
            Predicted class labels, shape (n_samples,).
        """
        approx = np.dot(X, self.w) - self.b
        return np.sign(approx)


# Example usage
if __name__ == "__main__":
    # Toy dataset
    X_train = np.array([[1, 2], [2, 3], [3, 3], [5, 4], [6, 6]])
    y_train = np.array([1, 1, 1, -1, -1])

    # Initialize and fit the model
    model = SVM(learning_rate=0.01, lambda_param=0.01, n_iters=1000)
    model.fit(X_train, y_train)

    # Predictions
    X_test = np.array([[3, 4], [4, 5]])
    predictions = model.predict(X_test)
    print("Predictions:", predictions)