import numpy as np
import lightgbm as lgb
import logging

class LightGBMModel:
    """LightGBM regression model."""
    def __init__(self):
        self.model = lgb.LGBMRegressor()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized LGBMRegressor.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """Fit the LightGBM model to the data."""
        try:
            self.model.fit(X, y)
            self.logger.info("Model fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during model fitting: {e}")
            raise

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict using the LightGBM model."""
        try:
            return self.model.predict(X)
        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            raise

    def score(self, X: np.ndarray, y: np.ndarray) -> float:
        """Score the LightGBM model."""
        try:
            return self.model.score(X, y)
        except Exception as e:
            self.logger.error(f"Error during scoring: {e}")
            raise