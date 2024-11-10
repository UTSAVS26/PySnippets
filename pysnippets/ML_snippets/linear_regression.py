import numpy as np

class LinearRegressionModel:
    """
    A simple linear regression model using the normal equation.
    """

    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Fit the linear regression model to the training data.

        Parameters:
        -----------
        X : np.ndarray
            Training data, shape (n_samples, n_features).
        y : np.ndarray
            Target values, shape (n_samples,).
        """
        # Add a column of ones to X for the intercept term
        X_b = np.c_[np.ones((X.shape[0], 1)), X]
        
        # Compute the optimal parameters using the pseudo-inverse for stability
        theta_best = np.linalg.pinv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
        
        # Set the intercept and coefficients
        self.intercept = theta_best[0]
        self.coefficients = theta_best[1:]

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict target values for the given test data.

        Parameters:
        -----------
        X : np.ndarray
            Test data, shape (n_samples, n_features).
        
        Returns:
        --------
        np.ndarray
            Predicted target values, shape (n_samples,).
        """
        return self.intercept + X.dot(self.coefficients)


# Example usage
if __name__ == "__main__":
    # Toy dataset
    X_train = np.array([[1], [2], [3], [4], [5]])
    y_train = np.array([1.5, 1.8, 3.2, 3.9, 5.1])

    # Initialize and fit the model
    model = LinearRegressionModel()
    model.fit(X_train, y_train)

    # Predictions
    X_test = np.array([[1.5], [3.5], [6]])
    predictions = model.predict(X_test)
    print("Predictions:", predictions)