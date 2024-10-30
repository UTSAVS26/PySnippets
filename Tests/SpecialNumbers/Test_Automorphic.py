import unittest
from Automorphic import is_automorphic 

class TestIsAutomorphic(unittest.TestCase):

    def test_case_automorphic_number(self):
        self.assertEqual(is_automorphic(25), "25 is an Automorphic number.")
        self.assertEqual(is_automorphic(5), "5 is an Automorphic number.")

    def test_case_non_automorphic_number(self):
        self.assertEqual(is_automorphic(16), "16 is not an Automorphic number.")
        self.assertEqual(is_automorphic(7), "7 is not an Automorphic number.")

    def test_case_single_digit_automorphic(self):
        self.assertEqual(is_automorphic(6), "6 is an Automorphic number.")  # 6^2 = 36

    def test_case_large_automorphic_number(self):
        self.assertEqual(is_automorphic(376), "376 is an Automorphic number.")  # 376^2 = 141376

    def test_case_large_non_automorphic_number(self):
        self.assertEqual(is_automorphic(123), "123 is not an Automorphic number.")

if __name__ == "__main__":
    unittest.main()
