import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import logging

class CVMeansModel:
    """Model to compute cross-validation mean score for Linear Regression."""

    def __init__(self):
        self.model = LinearRegression()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized LinearRegression model.")

    def cross_val_mean(self, X: np.ndarray, y: np.ndarray, cv: int = 5) -> float:
        """Compute the mean cross-validation score."""
        try:
            return np.mean(cross_val_score(self.model, X, y, cv=cv))
        except Exception as e:
            self.logger.error(f"Error during cross-validation: {e}")
            raise
