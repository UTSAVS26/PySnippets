import numpy as np
import lightgbm as lgb

class LightGBMModel:
    def __init__(self):
        self.model = lgb.LGBMRegressor()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)