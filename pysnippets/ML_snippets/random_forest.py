import numpy as np
from collections import Counter
from sklearn.tree import DecisionTreeClassifier

class RandomForest:
    """
    Random Forest Classifier.

    Parameters:
    -----------
    n_trees : int
        The number of trees in the forest.
    max_depth : int, optional
        The maximum depth of the individual trees.
    min_samples_split : int, optional
        The minimum number of samples required to split an internal node.
    bootstrap : bool, optional
        Whether to use bootstrap samples for each tree (default is True).
    """

    def __init__(self, n_trees: int = 10, max_depth: int = None, min_samples_split: int = 2, bootstrap: bool = True):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.bootstrap = bootstrap
        self.trees = []

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Fit the random forest to the training data.

        Parameters:
        -----------
        X : np.ndarray
            Training data, shape (n_samples, n_features).
        y : np.ndarray
            Target values, shape (n_samples,).
        """
        self.trees = []
        for _ in range(self.n_trees):
            # Generate bootstrap sample
            if self.bootstrap:
                indices = np.random.choice(len(X), len(X), replace=True)
            else:
                indices = np.arange(len(X))
            X_sample = X[indices]
            y_sample = y[indices]
            
            # Create and train a new decision tree
            tree = DecisionTreeClassifier(max_depth=self.max_depth, min_samples_split=self.min_samples_split)
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict class labels for the input samples.

        Parameters:
        -----------
        X : np.ndarray
            Input data, shape (n_samples, n_features).
        
        Returns:
        --------
        np.ndarray
            Predicted class labels, shape (n_samples,).
        """
        # Collect predictions from each tree
        tree_preds = np.array([tree.predict(X) for tree in self.trees])
        
        # Majority vote
        final_preds = np.apply_along_axis(lambda x: Counter(x).most_common(1)[0][0], axis=0, arr=tree_preds)
        return final_preds


# Example usage
if __name__ == "__main__":
    # Toy dataset
    X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y_train = np.array([0, 1, 0, 1])

    # Initialize and fit the model
    model = RandomForest(n_trees=5, max_depth=3, bootstrap=True)
    model.fit(X_train, y_train)

    # Predictions
    X_test = np.array([[2, 3], [6, 7]])
    predictions = model.predict(X_test)
    print("Predictions:", predictions)