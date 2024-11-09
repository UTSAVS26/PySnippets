import unittest
from pysnippets.Dynamic Programming.matrix_chain_multiplication import matrix_multiplication

class TestMatrixChainMultiplication(unittest.TestCase):

    def test_matrix_multiplication_case1(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(matrix_multiplication(arr, len(arr)), 38000)

    def test_matrix_multiplication_case2(self):
        arr = [10, 20, 30]
        self.assertEqual(matrix_multiplication(arr, len(arr)), 6000)

    def test_matrix_multiplication_case3(self):
        arr = [40, 20, 30, 10, 30]
        self.assertEqual(matrix_multiplication(arr, len(arr)), 26000)

    def test_matrix_multiplication_case4(self):
        arr = [10, 20, 30]
        self.assertEqual(matrix_multiplication(arr, len(arr)), 6000)

if __name__ == "__main__":
    unittest.main()
