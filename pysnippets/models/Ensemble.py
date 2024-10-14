import numpy as np
from sklearn.ensemble import RandomForestClassifier

class EnsembleModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)