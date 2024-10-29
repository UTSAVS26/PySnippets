import unittest
import time
from unittest.mock import patch
from pysnippets.Performance.memoize import memoize


class TestMemoize(unittest.TestCase):

    def test_memoization(self):
        @memoize
        def expensive_function(x, y):
            time.sleep(1)  # simulate an expensive operation
            return x + y

        # Mock time.sleep to avoid real delays
        with patch("time.sleep", return_value=None):
            # first call
            start = time.time()
            result1 = expensive_function(2, 3)
            duration1 = time.time() - start

            # second call with the same arguments
            start = time.time()
            result2 = expensive_function(2, 3)
            duration2 = time.time() - start

        # Verify that both results are the same
        self.assertEqual(result1, result2)
        # Ensure the cached call is significantly faster
        self.assertGreater(duration1, duration2)
        # Ensure the second call is almost instantaneous (cached)
        self.assertLess(duration2, 0.001)

    def test_different_arguments(self):
        @memoize
        def add(x, y):
            return x + y

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(2, 3), 5)  # should use cached result

    def test_with_kwargs(self):
        @memoize
        def greet(name, greeting="hello"):
            return f"{greeting}, {name}!"

        self.assertEqual(greet("alice"), "hello, alice!")
        self.assertEqual(greet("alice", greeting="hi"), "hi, alice!")
        # Cached result with default greeting
        self.assertEqual(greet("alice"), "hello, alice!")

    def test_complex_arguments(self):
        @memoize
        def process(data):
            return sum(data)

        # Test with a tuple (immutable) to ensure caching works with complex data types
        data = (1, 2, 3)
        self.assertEqual(process(data), 6)
        self.assertEqual(process(data), 6)  # should use cached result


if __name__ == "__main__":
    unittest.main()
