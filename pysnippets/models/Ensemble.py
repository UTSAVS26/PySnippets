import numpy as np
from sklearn.ensemble import RandomForestClassifier
import logging

class EnsembleModel:
    """
    Ensemble model using RandomForestClassifier.
    """

    def __init__(self):
        """
        Initialize the EnsembleModel with a RandomForestClassifier.
        """
        self.model = RandomForestClassifier()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized RandomForestClassifier.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the RandomForestClassifier model to the data.

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
        Predict using the RandomForestClassifier model.

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
        Score the RandomForestClassifier model.

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
