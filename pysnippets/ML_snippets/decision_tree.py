from collections import Counter
import numpy as np

class Node:
    """Represents a single node in the decision tree."""
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

    def is_leaf_node(self):
        """Check if the node is a leaf node."""
        return self.value is not None


class DecisionTreeClassifier:
    """
    A simple implementation of a Decision Tree Classifier.
    
    Parameters:
    -----------
    max_depth : int
        The maximum depth of the tree.
    """
    
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        """
        Build the decision tree classifier from the training set (X, y).
        
        Parameters:
        -----------
        X : np.ndarray
            Training features, shape (n_samples, n_features).
        y : np.ndarray
            Training labels, shape (n_samples,).
        """
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        """
        Predict class for X.
        
        Parameters:
        -----------
        X : np.ndarray
            Samples, shape (n_samples, n_features).
        
        Returns:
        --------
        np.ndarray
            Predicted classes, shape (n_samples,).
        """
        return np.array([self._traverse_tree(x, self.tree) for x in X])

    def _build_tree(self, X, y, depth=0):
        """
        Recursively build the decision tree.
        
        Parameters:
        -----------
        X : np.ndarray
            Features for the current node.
        y : np.ndarray
            Labels for the current node.
        depth : int
            The depth of the current node.
        
        Returns:
        --------
        Node
            The root node of the decision tree.
        """
        num_samples, num_features = X.shape
        num_labels = len(Counter(y))

        # Stopping criteria
        if num_labels == 1 or (self.max_depth is not None and depth >= self.max_depth):
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        # Find the best split
        best_feat, best_thresh = self._best_split(X, y, num_features)
        if best_feat is None:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        # Grow the children recursively
        indices_left = X[:, best_feat] <= best_thresh
        left = self._build_tree(X[indices_left], y[indices_left], depth + 1)
        right = self._build_tree(X[~indices_left], y[~indices_left], depth + 1)
        return Node(feature=best_feat, threshold=best_thresh, left=left, right=right)

    def _best_split(self, X, y, num_features):
        """
        Find the best feature and threshold to split on using Gini impurity.
        
        Parameters:
        -----------
        X : np.ndarray
            Features for the current node.
        y : np.ndarray
            Labels for the current node.
        num_features : int
            The number of features to consider for splitting.
        
        Returns:
        --------
        Tuple[int, float]
            The best feature index and the best threshold to split on.
        """
        best_feat, best_thresh, best_gini = None, None, 1

        for feat in range(num_features):
            thresholds, classes = zip(*sorted(zip(X[:, feat], y)))
            num_left = Counter()
            num_right = Counter(y)
            
            for i in range(1, len(y)):
                c = classes[i - 1]
                num_left[c] += 1
                num_right[c] -= 1

                gini_left = self._gini_impurity(num_left, i)
                gini_right = self._gini_impurity(num_right, len(y) - i)
                gini = (i * gini_left + (len(y) - i) * gini_right) / len(y)

                if thresholds[i] == thresholds[i - 1]:
                    continue
                if gini < best_gini:
                    best_feat, best_thresh, best_gini = feat, thresholds[i], gini
        return best_feat, best_thresh

    def _gini_impurity(self, class_counts, total_count):
        """
        Calculate the Gini impurity for a node.
        
        Parameters:
        -----------
        class_counts : Counter
            Counts of each class in the node.
        total_count : int
            Total number of samples in the node.
        
        Returns:
        --------
        float
            Gini impurity of the node.
        """
        return 1.0 - sum((count / total_count) ** 2 for count in class_counts.values())

    def _traverse_tree(self, x, node):
        """
        Traverse the tree to make a prediction.
        
        Parameters:
        -----------
        x : np.ndarray
            Single sample for which prediction is to be made.
        node : Node
            The current node in the tree.
        
        Returns:
        --------
        int
            Predicted class label.
        """
        if node.is_leaf_node():
            return node.value
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)


# Example usage
if __name__ == "__main__":
    # Toy dataset
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([0, 0, 1, 1])

    # Initialize and fit the model
    clf = DecisionTreeClassifier(max_depth=3)
    clf.fit(X_train, y_train)

    # Predictions
    X_test = np.array([[1.5, 2.5], [3.5, 4.5]])
    predictions = clf.predict(X_test)
    print("Predictions:", predictions)