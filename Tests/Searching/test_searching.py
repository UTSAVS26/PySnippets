import unittest
import sys
import os

# Add the parent directory of pysnippets to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pysnippets.Searching.Linear_Search import linear_search
from pysnippets.Searching.Jump_search import jump_search
from pysnippets.Searching.Interpolation import interpolation_search
from pysnippets.Searching.Exponential_search import exponential_search
from pysnippets.Searching.Fibonacci_search import fibonacci_search
from pysnippets.Searching.Ternary_search import ternary_search
from pysnippets.Searching.recursive_binary_search import binarySearchRecursive


class TestSearchingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.arr = [2, 3, 4, 10, 40]
        self.target = 10
        self.not_found_target = 5
        self.empty_arr = []
        self.single_element_arr = [10]
        self.target_at_start = 2
        self.target_at_end = 40

    def test_linear_search(self):
        self.assertEqual(linear_search(self.arr, self.target), 3)
        self.assertEqual(linear_search(self.arr, self.not_found_target), -1)
        self.assertEqual(linear_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(linear_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(linear_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(linear_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(linear_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_jump_search(self):
        self.assertEqual(jump_search(self.arr, self.target), 3)
        self.assertEqual(jump_search(self.arr, self.not_found_target), -1)
        self.assertEqual(jump_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(jump_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(jump_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(jump_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(jump_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_interpolation_search(self):
        self.assertEqual(interpolation_search(self.arr, self.target), 3)
        self.assertEqual(interpolation_search(self.arr, self.not_found_target), -1)
        self.assertEqual(interpolation_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(interpolation_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(interpolation_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(interpolation_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(interpolation_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_exponential_search(self):
        self.assertEqual(exponential_search(self.arr, self.target), 3)
        self.assertEqual(exponential_search(self.arr, self.not_found_target), -1)
        self.assertEqual(exponential_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(exponential_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(exponential_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(exponential_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(exponential_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_fibonacci_search(self):
        self.assertEqual(fibonacci_search(self.arr, self.target), 3)
        self.assertEqual(fibonacci_search(self.arr, self.not_found_target), -1)
        self.assertEqual(fibonacci_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(fibonacci_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(fibonacci_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(fibonacci_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(fibonacci_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_ternary_search(self):
        self.assertEqual(ternary_search(self.arr, self.target), 3)
        self.assertEqual(ternary_search(self.arr, self.not_found_target), -1)
        self.assertEqual(ternary_search(self.empty_arr, self.target), -1)  # Test empty array
        self.assertEqual(ternary_search(self.single_element_arr, self.target), 0)  # Test single element match
        self.assertEqual(ternary_search(self.single_element_arr, 5), -1)  # Test single element no match
        self.assertEqual(ternary_search(self.arr, self.target_at_start), 0)  # Test target at start
        self.assertEqual(ternary_search(self.arr, self.target_at_end), 4)  # Test target at end

    def test_recursive_binary_search(self):
        self.assertEqual(binarySearchRecursive(self.arr, 0, len(self.arr)-1, self.target), 3)
        self.assertEqual(binarySearchRecursive(self.arr, 0, len(self.arr)-1, self.not_found_target), -1)
        self.assertEqual(binarySearchRecursive(self.empty_arr, 0, len(self.empty_arr)-1, self.target), -1)  # Test empty array
        self.assertEqual(binarySearchRecursive(self.single_element_arr, 0, 0, self.target), 0)  # Test single element match
        self.assertEqual(binarySearchRecursive(self.single_element_arr, 0, 0, 5), -1)  # Test single element no match
        self.assertEqual(binarySearchRecursive(self.arr, 0, len(self.arr)-1, self.target_at_start), 0)  # Test target at start
        self.assertEqual(binarySearchRecursive(self.arr, 0, len(self.arr)-1, self.target_at_end), 4)  # Test target at end

if __name__ == '__main__':
    unittest.main()
