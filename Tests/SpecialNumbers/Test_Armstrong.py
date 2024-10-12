import unittest
from Armstrong import is_armstrong 

class TestIsArmstrong(unittest.TestCase):

    def test_case_armstrong_number(self):
        # Test with an Armstrong number (153)
        self.assertEqual(is_armstrong(153), "153 is an Armstrong number.")

    def test_case_non_armstrong_number(self):
        # Test with a non-Armstrong number (13)
        self.assertEqual(is_armstrong(13), "13 is not an Armstrong number.")

    def test_case_single_digit(self):
        # Test with a single digit number (all single digits are Armstrong numbers)
        self.assertEqual(is_armstrong(5), "5 is an Armstrong number.")

    def test_case_large_armstrong_number(self):
        # Test with a large Armstrong number (9474)
        self.assertEqual(is_armstrong(9474), "9474 is an Armstrong number.")

    def test_case_large_non_armstrong_number(self):
        # Test with a large non-Armstrong number (9475)
        self.assertEqual(is_armstrong(9475), "9475 is not an Armstrong number.")

if __name__ == "__main__":
    unittest.main()
