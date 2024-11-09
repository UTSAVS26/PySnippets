import unittest
from pysnippets.greedyalgorithms.fractional_knapsack import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):
    def test_case1(self):
        # Test Case 1: Basic test with known output
        W, n = 50, 3
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        result = fractional_knapsack(W, n, profits, weights)
        self.assertAlmostEqual(result, 240)

    def test_case2(self):
        # Test Case 2: Exact fit test case
        W, n = 30, 2
        profits = [40, 50]
        weights = [10, 20]
        result = fractional_knapsack(W, n, profits, weights)
        self.assertAlmostEqual(result, 90)

if __name__ == "__main__":
    unittest.main()
