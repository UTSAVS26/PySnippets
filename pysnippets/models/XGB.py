import numpy as np
import xgboost as xgb

class XGBModel:
    def __init__(self):
        self.model = xgb.XGBRegressor()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        return self.model.score(X, y)