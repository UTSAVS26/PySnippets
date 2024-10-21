import numpy as np
from catboost import CatBoostRegressor

class CatBoostModel:
    def __init__(self):
        self.model = CatBoostRegressor(silent=True)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)