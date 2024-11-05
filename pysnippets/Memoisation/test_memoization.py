import unittest
from fibonacci import fibonacci
from knapsack import knapsack
from lcs import lcs

class TestMemoization(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(30), 832040)

    def test_knapsack(self):
        weights = (1, 2, 3)
        values = (10, 15, 40)
        capacity = 6
        self.assertEqual(knapsack(weights, values, capacity, len(values)), 55)
        self.assertEqual(knapsack((1, 2, 3, 4), (10, 20, 30, 40), 6, 4), 60)

    def test_lcs(self):
        self.assertEqual(lcs("AGGTAB", "GXTXAYB", len("AGGTAB"), len("GXTXAYB")), 4)
        self.assertEqual(lcs("ABC", "AC", len("ABC"), len("AC")), 2)

if __name__ == "__main__":
    unittest.main() 