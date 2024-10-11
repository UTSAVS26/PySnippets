import unittest
from io import StringIO
import sys
import time
from pysnippets.Performance.timer import timer


class TestTimer(unittest.TestCase):

    # this method runs before every test case, used to setup any resources/environment
    def setUp(self):
        # Store the original sys.stdout so we can restore it later
        self.held = sys.stdout
        # Redirect sys.stdout to StringIO() to capture printed output
        sys.stdout = StringIO()

    # this method runs after every test case, used to teardown any resources/environment
    def tearDown(self):
        # Reset sys.stdout to the original value
        sys.stdout = self.held

    def test_timer_measures_time(self):
        with timer("Test operation"):
            time.sleep(0.1)

        output = sys.stdout.getvalue().strip()
        self.assertRegex(output, r"Test operation took \d+\.\d{2} seconds")

    def test_timer_default_description(self):
        with timer():
            pass

        output = sys.stdout.getvalue().strip()
        self.assertRegex(output, r"Execution took \d+\.\d{2} seconds")

    def test_timer_nested(self):
        with timer("Outer"):
            time.sleep(0.1)
            with timer("Inner"):
                time.sleep(0.1)

        output = sys.stdout.getvalue().strip().split("\n")
        self.assertEqual(len(output), 2)
        self.assertRegex(output[0], r"Inner took \d+\.\d{2} seconds")
        self.assertRegex(output[1], r"Outer took \d+\.\d{2} seconds")


if __name__ == "__main__":
    unittest.main()
