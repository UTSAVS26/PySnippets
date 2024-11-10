import unittest
import numpy as np
from library_snippets.numpy_snippet import add, multiply

class TestNumpySnippet(unittest.TestCase):
    def test_add(self):
        """ Test addition of two arrays. """
        result = add(np.array([1, 2, 3]), np.array([4, 5, 6]))
        np.testing.assert_array_equal(result, np.array([5, 7, 9]))

    def test_multiply(self):
        """ Test multiplication of two arrays. """
        result = multiply(np.array([1, 2, 3]), np.array([4, 5, 6]))
        np.testing.assert_array_equal(result, np.array([4, 10, 18]))

# Additional tests for subtract, divide, power, etc., can be added similarly.

if __name__ == '__main__':
    unittest.main() 