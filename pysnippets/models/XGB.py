import numpy as np
import xgboost as xgb
import logging

class XGBModel:
    """XGBoost regression model."""

    def __init__(self):
        self.model = xgb.XGBRegressor()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized XGBRegressor.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """Fit the XGBoost model to the data."""
        try:
            self.model.fit(X, y)
            self.logger.info("Model fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during model fitting: {e}")
            raise

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict using the XGBoost model."""
        try:
            return self.model.predict(X)
        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            raise

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Score the XGBoost model."""
        try:
            return self.model.score(X, y)
        except Exception as e:
            self.logger.error(f"Error during scoring: {e}")
            raise
