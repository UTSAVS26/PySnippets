import unittest
from pysnippets.math.vector_operations import vector_addition, vector_subtraction, scalar_multiplication, dot_product, vector_magnitude, vector_normalization, cross_product, angle_between_vectors, projection

class TestVectorOperations(unittest.TestCase):

    def test_vector_addition(self):
        # Normal case
        self.assertEqual(vector_addition([1, 2, 3], [4, 5, 6]), [5, 7, 9])

        # Case with floats
        self.assertEqual(vector_addition([1.5, 2.5], [3.5, 4.5]), [5.0, 7.0])

        # Dimension mismatch
        with self.assertRaises(ValueError):
            vector_addition([1, 2], [1, 2, 3])

    def test_vector_subtraction(self):
        # Normal case
        self.assertEqual(vector_subtraction([5, 7, 9], [4, 5, 6]), [1, 2, 3])

        # Case with floats
        self.assertEqual(vector_subtraction([3.5, 4.5], [1.5, 2.5]), [2.0, 2.0])

        # Dimension mismatch
        with self.assertRaises(ValueError):
            vector_subtraction([1, 2], [1, 2, 3])

    def test_scalar_multiplication(self):
        # Normal case
        self.assertEqual(scalar_multiplication([1, 2, 3], 3), [3, 6, 9])

        # Case with floats
        self.assertEqual(scalar_multiplication([1.5, 2.5], 2), [3.0, 5.0])

    def test_dot_product(self):
        # Normal case
        self.assertEqual(dot_product([1, 2, 3], [4, 5, 6]), 32)

        # Case with floats
        self.assertEqual(dot_product([1.5, 2.5], [3.5, 4.5]), 16.25)

        # Dimension mismatch
        with self.assertRaises(ValueError):
            dot_product([1, 2], [1, 2, 3])

    def test_vector_magnitude(self):
        # Normal case
        self.assertAlmostEqual(vector_magnitude([3, 4]), 5.0)

        # Case with floats
        self.assertAlmostEqual(vector_magnitude([1.5, 2.5]), math.sqrt(8.5))

    def test_vector_normalization(self):
        # Normal case
        self.assertAlmostEqual(vector_normalization([3, 4]), [0.6, 0.8])

        # Case with zero vector
        with self.assertRaises(ValueError):
            vector_normalization([0, 0])

    def test_cross_product(self):
        # Normal case
        self.assertEqual(cross_product([1, 0, 0], [0, 1, 0]), [0, 0, 1])

        # Dimension mismatch
        with self.assertRaises(ValueError):
            cross_product([1, 2], [1, 2, 3])

    def test_angle_between_vectors(self):
        # Normal case
        self.assertAlmostEqual(angle_between_vectors([1, 0], [0, 1]), math.pi / 2)

        # Case with parallel vectors
        self.assertAlmostEqual(angle_between_vectors([1, 0], [2, 0]), 0.0)

    def test_projection(self):
        # Normal case
        self.assertAlmostEqual(projection([1, 2, 3], [4, 5, 6]), [0.6623, 0.8279, 0.9935], places=4)

        # Dimension mismatch
        with self.assertRaises(ValueError):
            projection([1, 2], [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
