import unittest
from Num_conversion.octal_to_decimal import octal_to_decimal

class TestOctalToDecimal(unittest.TestCase):
    def test_valid_octal(self):
        self.assertEqual(octal_to_decimal("32"), 26)
    
    def test_invalid_octal(self):
        self.assertEqual(octal_to_decimal("8"), "Invalid octal number")
    
    def test_empty_string(self):
        self.assertEqual(octal_to_decimal(""), "Invalid octal number")

if __name__ == '__main__':
    unittest.main()