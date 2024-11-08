import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
import logging

class GridSearchModel:
    """
    Grid search model for Logistic Regression.
    """

    def __init__(self):
        """
        Initialize the GridSearchModel with a LogisticRegression model and a parameter grid.
        """
        self.model = LogisticRegression()
        self.param_grid = {'C': [0.1, 1, 10]}
        self.grid_search = GridSearchCV(self.model, self.param_grid)
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initialized LogisticRegression model with GridSearchCV.")

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Fit the GridSearchCV to the data.

        Parameters:
        X (np.ndarray): The feature matrix.
        y (np.ndarray): The target vector.
        """
        try:
            self.grid_search.fit(X, y)
            self.logger.info("Grid search fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during grid search fitting: {e}")
            raise

    def best_params(self) -> dict:
        """
        Retrieve the best parameters found by grid search.

        Returns:
        dict: A dictionary containing the best parameters.
        """
        try:
            return self.grid_search.best_params_
        except Exception as e:
            self.logger.error(f"Error retrieving best parameters: {e}")
            raise