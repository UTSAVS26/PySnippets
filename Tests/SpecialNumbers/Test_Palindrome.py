import unittest
from Palindrome import is_palindrome 
from io import StringIO
import sys

class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.held

    def test_case_palindrome_number(self):
        is_palindrome(101)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "101 is a palindrome.")

        is_palindrome(12321)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "12321 is a palindrome.")

    def test_case_non_palindrome_number(self):
        is_palindrome(10)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "10 is not a palindrome.")

        is_palindrome(123)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "123 is not a palindrome.")

if __name__ == "__main__":
    unittest.main()
