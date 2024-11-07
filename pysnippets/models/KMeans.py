import numpy as np
from sklearn.cluster import KMeans
import logging

class KMeansModel:
    """
    KMeans clustering model.
    """

    def __init__(self, n_clusters: int = 3):
        """
        Initialize the KMeansModel with a specified number of clusters.

        Parameters:
        n_clusters (int): The number of clusters to form and the number of centroids to generate.
        """
        self.model = KMeans(n_clusters=n_clusters)
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"Initialized KMeans with n_clusters={n_clusters}.")

    def fit(self, X: np.ndarray) -> None:
        """
        Fit the KMeans model to the data.

        Parameters:
        X (np.ndarray): The feature matrix.
        """
        try:
            self.model.fit(X)
            self.logger.info("Model fitting successful.")
        except Exception as e:
            self.logger.error(f"Error during model fitting: {e}")
            raise

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict cluster indices for samples.

        Parameters:
        X (np.ndarray): The feature matrix.

        Returns:
        np.ndarray: The predicted cluster indices.
        """
        try:
            return self.model.predict(X)
        except Exception as e:
            self.logger.error(f"Error during prediction: {e}")
            raise
