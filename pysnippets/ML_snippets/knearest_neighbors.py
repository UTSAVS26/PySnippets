import numpy as np
from collections import Counter

class KNearestNeighbors:
    """
    K-Nearest Neighbors classifier.

    Parameters:
    -----------
    k : int
        Number of neighbors to use for prediction.
    """

    def __init__(self, k: int = 3):
        if k <= 0:
            raise ValueError("k must be greater than 0")
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Store the training data.
        
        Parameters:
        -----------
        X : np.ndarray
            Training data, shape (n_samples, n_features).
        y : np.ndarray
            Training labels, shape (n_samples,).
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict the class labels for the provided data.
        
        Parameters:
        -----------
        X : np.ndarray
            Test data, shape (n_samples, n_features).
        
        Returns:
        --------
        np.ndarray
            Predicted class labels, shape (n_samples,).
        """
        predictions = [self._predict_single(x) for x in X]
        return np.array(predictions)

    def _predict_single(self, x: np.ndarray) -> int:
        """
        Predict the class label for a single test sample.
        
        Parameters:
        -----------
        x : np.ndarray
            Single test sample, shape (n_features,).
        
        Returns:
        --------
        int
            Predicted class label.
        """
        # Calculate distances between x and all samples in the training set
        distances = np.linalg.norm(self.X_train - x, axis=1)
        
        # Find the k nearest neighbors and their labels
        k_indices = distances.argsort()[:self.k]
        k_nearest_labels = self.y_train[k_indices]
        
        # Return the most common label among the neighbors
        most_common = Counter(k_nearest_labels).most_common(1)[0][0]
        return most_common


# Example usage
if __name__ == "__main__":
    # Toy dataset
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([0, 0, 1, 1])

    # Initialize and fit the model
    knn = KNearestNeighbors(k=3)
    knn.fit(X_train, y_train)

    # Predictions
    X_test = np.array([[1.5, 2.5], [3.5, 4.5]])
    predictions = knn.predict(X_test)
    print("Predictions:", predictions)