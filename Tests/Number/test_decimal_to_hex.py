import unittest
from Num_conversion.decimal_to_hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_valid_decimal(self):
        self.assertEqual(decimal_to_hex(26), "1A")
    
    def test_invalid_decimal(self):
        self.assertEqual(decimal_to_hex("26"), "Invalid decimal number")
    
    def test_negative_decimal(self):
        self.assertEqual(decimal_to_hex(-26), "Invalid decimal number")

if __name__ == '__main__':
    unittest.main()