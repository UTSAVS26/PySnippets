import unittest

from Interpolation import interpolation_search
from Jump_search import jump_search
from Ternary_search import ternary_search
from Linear_Search import linear_search
from iterative_binary_search import binary_search_iterative
from Exponential_search import exponential_search
from Fibonacci_search import fibonacci_search

# Optionally, if you have a recursive binary search, import it as well
# from .recursive_binary_search import binary_search_recursive

class TestSearchAlgorithms(unittest.TestCase):

    def setUp(self):
        self.arr = [2, 3, 4, 10, 40]
        self.target_present = 10
        self.target_absent = 5

    def test_linear_search_present(self):
        result = linear_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_linear_search_absent(self):
        result = linear_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_iterative_binary_search_present(self):
        result = binary_search_iterative(self.arr, 0, len(self.arr)-1, self.target_present)
        self.assertEqual(result, 3)

    def test_iterative_binary_search_absent(self):
        result = binary_search_iterative(self.arr, 0, len(self.arr)-1, self.target_absent)
        self.assertEqual(result, -1)

    def test_exponential_search_present(self):
        result = exponential_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_exponential_search_absent(self):
        result = exponential_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_fibonacci_search_present(self):
        result = fibonacci_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_fibonacci_search_absent(self):
        result = fibonacci_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_jump_search_present(self):
        result = jump_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_jump_search_absent(self):
        result = jump_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_interpolation_search_present(self):
        result = interpolation_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_interpolation_search_absent(self):
        result = interpolation_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_ternary_search_present(self):
        result = ternary_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_ternary_search_absent(self):
        result = ternary_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    # If you have recursive_binary_search, add tests for it as well
    # def test_recursive_binary_search_present(self):
    #     result = binary_search_recursive(self.arr, 0, len(self.arr)-1, self.target_present)
    #     self.assertEqual(result, 3)

    # def test_recursive_binary_search_absent(self):
    #     result = binary_search_recursive(self.arr, 0, len(self.arr)-1, self.target_absent)
    #     self.assertEqual(result, -1)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()