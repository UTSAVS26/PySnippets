from collections import Counter
import numpy as np

class DecisionTreeClassifier:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y)

    def predict(self, X):
        return np.array([self._traverse_tree(x, self.tree) for x in X])

    def _build_tree(self, X, y, depth=0):
        num_samples, num_features = X.shape
        num_labels = len(Counter(y))
        if num_labels == 1 or (self.max_depth is not None and depth >= self.max_depth):
            return Counter(y).most_common(1)[0][0]
        best_feat, best_thresh = self._best_split(X, y, num_features)
        if best_feat is None:
            return Counter(y).most_common(1)[0][0]
        indices_left = X[:, best_feat] <= best_thresh
        left = self._build_tree(X[indices_left], y[indices_left], depth + 1)
        right = self._build_tree(X[~indices_left], y[~indices_left], depth + 1)
        return {'feature': best_feat, 'threshold': best_thresh, 'left': left, 'right': right}

    def _best_split(self, X, y, num_features):
        best_feat, best_thresh, best_gini = None, None, 1
        for feat in range(num_features):
            thresholds, classes = zip(*sorted(zip(X[:, feat], y)))
            num_left = Counter()
            num_right = Counter(y)
            for i in range(1, len(y)):
                c = classes[i - 1]
                num_left[c] += 1
                num_right[c] -= 1
                gini_left = 1.0 - sum((count / i) ** 2 for count in num_left.values())
                gini_right = 1.0 - sum((count / (len(y) - i)) ** 2 for count in num_right.values())
                gini = (i * gini_left + (len(y) - i) * gini_right) / len(y)
                if thresholds[i] == thresholds[i - 1]:
                    continue
                if gini < best_gini:
                    best_feat, best_thresh, best_gini = feat, thresholds[i], gini
        return best_feat, best_thresh

    def _traverse_tree(self, x, node):
        if isinstance(node, dict):
            if x[node['feature']] <= node['threshold']:
                return self._traverse_tree(x, node['left'])
            else:
                return self._traverse_tree(x, node['right'])
        return node 