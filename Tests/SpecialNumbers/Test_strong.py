import unittest
from Strong import is_strong  
from io import StringIO
import sys

class TestIsStrong(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        # Restore original stdout
        sys.stdout = self.held

    def test_case_strong_number(self):
        is_strong(145)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "145 is a Strong number.")

        is_strong(1)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "1 is a Strong number.")

    def test_case_non_strong_number(self):
        is_strong(134)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "134 is not a Strong number.")

        is_strong(10)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "10 is not a Strong number.")

if __name__ == "__main__":
    unittest.main()
