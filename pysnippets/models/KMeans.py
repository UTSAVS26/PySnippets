import numpy as np
from sklearn.cluster import KMeans

class KMeansModel:
    def __init__(self, n_clusters=3):
        self.model = KMeans(n_clusters=n_clusters)

    def fit(self, X):
        self.model.fit(X)

    def predict(self, X):
        return self.model.predict(X)