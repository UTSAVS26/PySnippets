import unittest
import time
from pysnippets.utilities.timer import time_execution
from io import StringIO
import sys


class TestTimeExecution(unittest.TestCase):

    def test_time_execution_output(self):
        @time_execution
        def slow_function(x: int) -> int:
            time.sleep(1)
            return x * 2

        captured_output = StringIO()
        sys.stdout = captured_output
        result = slow_function(5)
        sys.stdout = sys.__stdout__

        self.assertEqual(result, 10)
        output = captured_output.getvalue()
        self.assertIn("Execution time", output)


if __name__ == "__main__":
    unittest.main()
