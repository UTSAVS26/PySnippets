import unittest
from utils import parse_complex

class TestUtils(unittest.TestCase):

    def test_parse_valid_positive(self):
        c = parse_complex("3 + 4i")
        self.assertEqual(c.real, 3)
        self.assertEqual(c.imaginary, 4)

    def test_parse_valid_negative(self):
        c = parse_complex("5 - 6i")
        self.assertEqual(c.real, 5)
        self.assertEqual(c.imaginary, -6)

    def test_parse_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_complex("invalid")

    def test_parse_missing_imaginary(self):
        with self.assertRaises(ValueError):
            parse_complex("3 + i")

    def test_parse_missing_real(self):
        with self.assertRaises(ValueError):
            parse_complex("+ 4i")

if __name__ == '__main__':
    unittest.main() 