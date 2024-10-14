import numpy as np
import unittest
from pysnippets.models.Grid_search import GridSearchModel  # Updated import

class TestGridSearchModel(unittest.TestCase):
    def setUp(self):
        self.model = GridSearchModel()
        self.X = np.random.rand(100, 2)
        self.y = (self.X[:, 0] + self.X[:, 1] > 1).astype(int)

    def test_fit(self):
        self.model.fit(self.X, self.y)
        best_params = self.model.best_params()
        self.assertIn('C', best_params)

if __name__ == '__main__':
    unittest.main()