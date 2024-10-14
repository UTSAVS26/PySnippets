import unittest
from Neon import is_neon
from io import StringIO
import sys

class TestIsNeon(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.held

    def test_case_neon_number(self):
        is_neon(9)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "9 is a Neon number.")

        is_neon(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 is a Neon number.")

    def test_case_non_neon_number(self):
        is_neon(20)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "20 is not a Neon number.")

        is_neon(5)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "5 is not a Neon number.")

    def test_case_large_non_neon_number(self):
        is_neon(100)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "100 is not a Neon number.")

if __name__ == "__main__":
    unittest.main()
