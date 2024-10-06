import unittest
from snippets.matrix_operations import add_matrices, multiply_matrices, transpose_matrix

class TestMatrixOperations(unittest.TestCase):

    def test_add_matrices(self):
        # Test case for normal behavior
        self.assertEqual(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

    def test_multiply_matrices(self):
        # Test case for normal behavior
        self.assertEqual(multiply_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

    def test_transpose_matrix(self):
        # Test case for normal behavior
        self.assertEqual(transpose_matrix([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_add_matrices_invalid(self):
        # Test case for invalid input
        with self.assertRaises(ValueError):
            add_matrices([[1, 2]], [[3, 4], [5, 6]])

if __name__ == '__main__':
    unittest.main()
