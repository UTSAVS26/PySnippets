import unittest
from pysnippets.Numbers.prime_factorization import prime_factorization

class TestPrimeFactorization(unittest.TestCase):

    def test_case_valid(self):
        self.assertEqual(prime_factorization(28), [2, 2, 7])
        self.assertEqual(prime_factorization(13), [13])

    def test_case_invalid_negative(self):
        with self.assertRaises(ValueError):
            prime_factorization(-10)

    def test_case_invalid_non_integer(self):
        with self.assertRaises(TypeError):
            prime_factorization("string")

    def test_case_large_number(self):
        self.assertEqual(prime_factorization(100), [2, 2, 5, 5])


if __name__ == "__main__":
    unittest.main()
