import numpy as np
from sklearn.linear_model import LogisticRegression
import logging

class LogisticModel:
    """
    Logistic Regression model.
    """

    def __init__(self):
        """
        Initialize the LogisticModel with a LogisticRegression model.
        """
        self.model = LogisticRegression()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized LogisticRegression model.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the Logistic Regression model to the data.

        Parameters:
        X (np.ndarray): The feature matrix.
        y (np.ndarray): The target vector.
        """
        try:
            self.model.fit(X, y)
            self.logger.info("Model fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during model fitting: {e}")
            raise

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict using the Logistic Regression model.

        Parameters:
        X (np.ndarray): The feature matrix.

        Returns:
        np.ndarray: The predicted values.
        """
        try:
            return self.model.predict(X)
        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            raise

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Score the Logistic Regression model.

        Parameters:
        X (np.ndarray): The feature matrix.
        y (np.ndarray): The target vector.

        Returns:
        float: The model's score.
        """
        try:
            return self.model.score(X, y)
        except Exception as e:
            self.logger.error(f"Error during scoring: {e}")
            raise
