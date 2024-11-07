import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

class GridSearchModel:
    def __init__(self):
        self.model = LogisticRegression()
        self.param_grid = {'C': [0.1, 1, 10]}
        self.grid_search = GridSearchCV(self.model, self.param_grid)

    def fit(self, X, y):
        self.grid_search.fit(X, y)

    def best_params(self):
        return self.grid_search.best_params_