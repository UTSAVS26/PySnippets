import unittest
import time
from pysnippets.Performance.memoize import memoize


class TestMemoize(unittest.TestCase):

    def test_memoization(self):
        @memoize
        def expensive_function(x, y):
            time.sleep(1)  # simulate an expensive operation
            return x + y

        # first call
        start = time.time()
        result1 = expensive_function(2, 3)
        duration1 = time.time() - start

        # second call with the same arguments
        start = time.time()
        result2 = expensive_function(2, 3)
        duration2 = time.time() - start

        self.assertEqual(result1, result2)  # results should be the same
        self.assertGreater(duration1, duration2)  # second call should be faster
        self.assertLess(
            duration2, 0.01
        )  # second call should be very fast (almost instant)

    def test_different_arguments(self):
        @memoize
        def add(x, y):
            return x + y

        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(2, 3), 5)  # this should use cached result

    def test_with_kwargs(self):
        @memoize
        def greet(name, greeting="hello"):
            return f"{greeting}, {name}!"

        self.assertEqual(greet("alice"), "hello, alice!")
        self.assertEqual(greet("alice", greeting="hi"), "hi, alice!")
        self.assertEqual(
            greet("alice"), "hello, alice!"
        )  # this should use cached result


if __name__ == "__main__":
    unittest.main()
