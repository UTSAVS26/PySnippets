import unittest
from complex_number_operations import add_complex, multiply_complex
from determinant import determinant
from fibonacci_sequence import fibonacci_sequence
from matrix_operations import matrix_addition, matrix_multiplication
from pascals_triangle import pascals_triangle
from vector_operations import vector_addition

class TestMathematics(unittest.TestCase):

    # Tests for Complex Number Operations
    def test_add_complex(self):
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))

    def test_multiply_complex(self):
        self.assertEqual(multiply_complex((1, 2), (3, 4)), (-5, 10))

    def test_add_complex_invalid(self):
        with self.assertRaises(TypeError):
            add_complex((1, 2), "string")

    # Tests for Determinant
    def test_determinant_2x2(self):
        self.assertEqual(determinant([[1, 2], [3, 4]]), -2)

    def test_determinant_3x3(self):
        self.assertEqual(determinant([[1, 2, 3], [0, 1, 4], [5, 6, 0]]), 1)  # Corrected expected value

    def test_determinant_invalid(self):
        with self.assertRaises(ValueError):
            determinant([[1, 2], [3]])

    # Tests for Fibonacci Sequence
    def test_fibonacci_sequence_count(self):
        self.assertEqual(fibonacci_sequence(count=10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_fibonacci_sequence_max_value(self):
        self.assertEqual(fibonacci_sequence(max_value=20), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_fibonacci_sequence_invalid(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence()

    # Tests for Matrix Operations
    def test_add_matrices(self):
        self.assertEqual(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

    def test_multiply_matrices(self):
        self.assertEqual(matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[19, 22], [43, 50]])

    def test_add_matrices_invalid(self):
        with self.assertRaises(ValueError):
            matrix_addition([[1, 2]], [[3, 4], [5, 6]])

    # Tests for Pascal's Triangle
    def test_pascals_triangle(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(pascals_triangle(5), expected)

    def test_pascals_triangle_invalid(self):
        with self.assertRaises(ValueError):
            pascals_triangle(0)

    # Tests for Vector Operations
    def test_vector_addition(self):
        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])

    def test_vector_addition_invalid(self):
        with self.assertRaises(ValueError):
            vector_addition([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main() 