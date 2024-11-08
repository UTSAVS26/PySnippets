import unittest
from Num_conversion.hex_to_decimal import hex_to_decimal

class TestHexToDecimal(unittest.TestCase):
    def test_valid_hex(self):
        self.assertEqual(hex_to_decimal("1A"), 26)
    
    def test_invalid_hex(self):
        self.assertEqual(hex_to_decimal("G"), "Invalid hexadecimal number")
    
    def test_empty_string(self):
        self.assertEqual(hex_to_decimal(""), "Invalid hexadecimal number")

if __name__ == '__main__':
    unittest.main()