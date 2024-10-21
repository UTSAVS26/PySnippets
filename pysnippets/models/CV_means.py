import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

class CVMeansModel:
    def __init__(self):
        self.model = LinearRegression()

    def cross_val_mean(self, X, y, cv=5):
        return np.mean(cross_val_score(self.model, X, y, cv=cv))