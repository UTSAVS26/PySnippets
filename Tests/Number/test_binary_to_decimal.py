import unittest
from ....pysnippets.Num_conversion.binary_to_decimal import binary_to_decimal

class TestBinaryToDecimal(unittest.TestCase):
    def test_valid_binary(self):
        self.assertEqual(binary_to_decimal("1010"), 10)
    
    def test_invalid_binary(self):
        self.assertEqual(binary_to_decimal("2"), "Invalid binary number")
    
    def test_empty_string(self):
        self.assertEqual(binary_to_decimal(""), "Invalid binary number")

if __name__ == '__main__':
    unittest.main()