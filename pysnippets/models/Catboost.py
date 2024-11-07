import numpy as np
from catboost import CatBoostRegressor
import logging

class CatBoostModel:
    """
    CatBoost regression model.
    """
    def __init__(self):
        self.model = CatBoostRegressor(silent=True)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized CatBoostRegressor.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the CatBoost model to the data.
        """
        try:
            self.model.fit(X, y)
            self.logger.info("Model fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during model fitting: {e}")
            raise

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict using the CatBoost model.
        """
        try:
            return self.model.predict(X)
        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            raise

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """
        Score the CatBoost model.
        """
        try:
            return self.model.score(X, y)
        except Exception as e:
            self.logger.error(f"Error during scoring: {e}")
            raise
