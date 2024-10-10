import unittest
from pysnippets.maths.complex_number_operations import (
    add_complex,
    subtract_complex,
    multiply_complex,
    divide_complex,
    conjugate_complex,
    modulus_complex,
    argument_complex,
)


class TestComplexNumbers(unittest.TestCase):

    def test_add_complex(self):
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))

    def test_add_complex_invalid(self):
        with self.assertRaises(TypeError):
            add_complex((1, 2), "string")

    def test_subtract_complex(self):
        self.assertEqual(subtract_complex((5, 7), (2, 3)), (3, 4))

    def test_subtract_complex_invalid(self):
        with self.assertRaises(TypeError):
            subtract_complex((1, 2), "invalid")

    def test_multiply_complex(self):
        self.assertEqual(multiply_complex((1, 2), (3, 4)), (-5, 10))

    def test_multiply_complex_invalid(self):
        with self.assertRaises(TypeError):
            multiply_complex((1, 2), "invalid")

    def test_divide_complex(self):
        self.assertEqual(divide_complex((3, 4), (1, 2)), (2.2, -0.4))

    def test_divide_complex_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_complex((3, 4), (0, 0))

    def test_conjugate_complex(self):
        self.assertEqual(conjugate_complex((3, 4)), (3, -4))

    def test_conjugate_complex_invalid(self):
        with self.assertRaises(TypeError):
            conjugate_complex("invalid")

    def test_modulus_complex(self):
        self.assertEqual(modulus_complex((3, 4)), 5.0)

    def test_modulus_complex_invalid(self):
        with self.assertRaises(TypeError):
            modulus_complex("invalid")

    def test_argument_complex(self):
        self.assertAlmostEqual(argument_complex((3, 4)), 0.927, places=3)

    def test_argument_complex_invalid(self):
        with self.assertRaises(TypeError):
            argument_complex("invalid")


if __name__ == "__main__":
    unittest.main()
