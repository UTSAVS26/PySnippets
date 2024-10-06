# test_number_formatting.py

import unittest
from pysnippets.Numbers.number_formatting import format_number


class TestNumberFormatting(unittest.TestCase):

    def test_format_integer(self):
        self.assertEqual(format_number(1234567), "1,234,567")

    def test_format_float(self):
        self.assertEqual(format_number(1234567.89), "1,234,567.89")

    def test_negative_number(self):
        self.assertEqual(format_number(-1234567), "-1,234,567")


if __name__ == "__main__":
    unittest.main()
