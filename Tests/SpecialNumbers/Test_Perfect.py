import unittest
from PerfectNumber import is_perfect  
from io import StringIO
import sys

class TestIsPerfect(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.held

    def test_case_perfect_number(self):
        is_perfect(6)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "6 is a Perfect number.")

        is_perfect(28)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "28 is a Perfect number.")

    def test_case_non_perfect_number(self):
        is_perfect(20)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "20 is not a Perfect number.")

        is_perfect(12)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "12 is not a Perfect number.")

if __name__ == "__main__":
    unittest.main()
