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

    # Test cases for search algorithms with target present
    def test_linear_search_present(self):
        result = linear_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_iterative_binary_search_present(self):
        result = binary_search_iterative(self.arr, 0, len(self.arr)-1, self.target_present)
        self.assertEqual(result, 3)

    def test_exponential_search_present(self):
        result = exponential_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_fibonacci_search_present(self):
        result = fibonacci_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_jump_search_present(self):
        result = jump_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_interpolation_search_present(self):
        result = interpolation_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    def test_ternary_search_present(self):
        result = ternary_search(self.arr, self.target_present)
        self.assertEqual(result, 3)

    # Test cases for search algorithms with target absent
    def test_linear_search_absent(self):
        result = linear_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_iterative_binary_search_absent(self):
        result = binary_search_iterative(self.arr, 0, len(self.arr)-1, self.target_absent)
        self.assertEqual(result, -1)

    def test_exponential_search_absent(self):
        result = exponential_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_fibonacci_search_absent(self):
        result = fibonacci_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_jump_search_absent(self):
        result = jump_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_interpolation_search_absent(self):
        result = interpolation_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    def test_ternary_search_absent(self):
        result = ternary_search(self.arr, self.target_absent)
        self.assertEqual(result, -1)

    # Edge case: Empty list
    def test_linear_search_empty(self):
        result = linear_search([], self.target_present)
        self.assertEqual(result, -1)

    def test_iterative_binary_search_empty(self):
        result = binary_search_iterative([], 0, -1, self.target_present)
        self.assertEqual(result, -1)

    def test_exponential_search_empty(self):
        result = exponential_search([], self.target_present)
        self.assertEqual(result, -1)

    def test_fibonacci_search_empty(self):
        result = fibonacci_search([], self.target_present)
        self.assertEqual(result, -1)

    def test_jump_search_empty(self):
        result = jump_search([], self.target_present)
        self.assertEqual(result, -1)

    def test_interpolation_search_empty(self):
        result = interpolation_search([], self.target_present)
        self.assertEqual(result, -1)

    def test_ternary_search_empty(self):
        result = ternary_search([], self.target_present)
        self.assertEqual(result, -1)

    # Edge case: Single-element list
    def test_linear_search_single_element_present(self):
        result = linear_search([10], self.target_present)
        self.assertEqual(result, 0)

    def test_linear_search_single_element_absent(self):
        result = linear_search([5], self.target_present)
        self.assertEqual(result, -1)

    def test_iterative_binary_search_single_element_present(self):
        result = binary_search_iterative([10], 0, 0, self.target_present)
        self.assertEqual(result, 0)

    def test_iterative_binary_search_single_element_absent(self):
        result = binary_search_iterative([5], 0, 0, self.target_present)
        self.assertEqual(result, -1)

    # Edge case: Duplicate values
    def test_linear_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = linear_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_iterative_binary_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = binary_search_iterative(arr, 0, len(arr)-1, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_exponential_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = exponential_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_fibonacci_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = fibonacci_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_jump_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = jump_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_interpolation_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = interpolation_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    def test_ternary_search_duplicates(self):
        arr = [2, 3, 3, 3, 40]
        result = ternary_search(arr, 3)
        self.assertEqual(result, 1)  # First occurrence of 3

    # Performance Test: Large List (Optional)
    def test_large_input(self):
        arr = list(range(1, 1000000))
        result = binary_search_iterative(arr, 0, len(arr) - 1, 999999)
        self.assertEqual(result, 999998)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()