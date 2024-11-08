import unittest
from Num_conversion.decimal_to_binary import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):
    def test_valid_decimal(self):
        self.assertEqual(decimal_to_binary(10), "1010")
    
    def test_invalid_decimal(self):
        self.assertEqual(decimal_to_binary("10"), "Invalid decimal number")
    
    def test_negative_decimal(self):
        self.assertEqual(decimal_to_binary(-10), "Invalid decimal number")

if __name__ == '__main__':
    unittest.main()