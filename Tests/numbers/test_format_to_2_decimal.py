
import unittest
from format_to_2_decimal import format_to_2_decimal

class TestFormatTo2Decimal(unittest.TestCase):
    def test_format_to_2_decimal(self):
        self.assertEqual(format_to_2_decimal(123.456), "123.46")
        self.assertEqual(format_to_2_decimal(123), "123.00")
        self.assertEqual(format_to_2_decimal(-123.456), "-123.46")

if __name__ == '__main__':
    unittest.main()
