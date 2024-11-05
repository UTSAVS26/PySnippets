import unittest
from format_to_2_decimal import format_to_2_decimal
from number_formatting import format_number
from pad_with_zeros import pad_with_zeros
from percentage_format import percentage_format
from prime_factorization import prime_factorization

class TestNumberFormatting(unittest.TestCase):

    def test_format_to_2_decimal(self):
        test_cases = [
            (123.456, '123.46'),
            (123, '123.00'),
            (-123.456, '-123.46')
        ]
        for num, expected in test_cases:
            self.assertEqual(format_to_2_decimal(num), expected)

    def test_format_number(self):
        test_cases = [
            (1234567, '1,234,567'),
            (12345.6789, '12 345,6789', {'thousands_sep': ' ', 'decimal_sep': ','})
        ]
        for num, expected, *args in test_cases:
            self.assertEqual(format_number(num, **(args[0] if args else {})), expected)

    def test_pad_with_zeros(self):
        test_cases = [
            (123, 6, '000123'),
            (1, 3, '001')
        ]
        for num, width, expected in test_cases:
            self.assertEqual(pad_with_zeros(num, width), expected)

    def test_percentage_format(self):
        test_cases = [
            (50, 200, '25.00%'),
            (1, 3, 3, '33.333%')
        ]
        for num, total, *args in test_cases:
            self.assertEqual(percentage_format(num, total, *(args if args else [])), expected)

    def test_prime_factorization(self):
        test_cases = [
            (28, [2, 2, 7]),
            (1, []),
            (13, [13])
        ]
        for num, expected in test_cases:
            self.assertEqual(prime_factorization(num), expected)

if __name__ == '__main__':
    unittest.main() 