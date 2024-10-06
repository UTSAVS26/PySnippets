import unittest
from pysnippets.maths.matrix_operations import matrix_multiplication, matrix_addition, matrix_transpose

class TestMatrixOperations(unittest.TestCase):

    def test_add_matrices(self):
        # Test case for normal behavior
        self.assertEqual(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

    def test_multiply_matrices(self):
        # Test case for normal behavior
        self.assertEqual(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

    def test_transpose_matrix(self):
        # Test case for normal behavior
        self.assertEqual(matrix_transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_add_matrices_invalid(self):
        # Test case for invalid input
        with self.assertRaises(ValueError):
            matrix_addition([[1, 2]], [[3, 4], [5, 6]])

if __name__ == '__main__':
    unittest.main()
