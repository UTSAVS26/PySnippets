import unittest
from pysnippets.algorithms.nqueen import n_queens

class TestNQueens(unittest.TestCase):
    def test_n_queens_4(self):
        """Test 4-Queens problem has exactly 2 solutions."""
        solutions = n_queens(4)
        self.assertEqual(len(solutions), 2)

    def test_n_queens_5(self):
        """Test 5-Queens problem has exactly 10 solutions."""
        solutions = n_queens(5)
        self.assertEqual(len(solutions), 10)

    def test_n_queens_1(self):
        """Test 1-Queen problem has exactly 1 solution."""
        solutions = n_queens(1)
        self.assertEqual(len(solutions), 1)

if __name__ == "__main__":
    unittest.main()
