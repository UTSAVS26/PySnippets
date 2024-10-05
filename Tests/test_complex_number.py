import unittest
from snippets.complex_numbers import add_complex, multiply_complex

class TestComplexNumbers(unittest.TestCase):

    def test_add_complex(self):
        # Test case for normal behavior
        self.assertEqual(add_complex((1, 2), (3, 4)), (4, 6))

    def test_multiply_complex(self):
        # Test case for normal behavior
        self.assertEqual(multiply_complex((1, 2), (3, 4)), (-5, 10))

    def test_add_complex_invalid(self):
        # Test case for invalid input
        with self.assertRaises(TypeError):
            add_complex((1, 2), "string")

if __name__ == '__main__':
    unittest.main()
