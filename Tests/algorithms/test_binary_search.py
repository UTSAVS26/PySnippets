import unittest
from pysnippets.algorithms.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_case_1(self):
        # Test case for normal behavior
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_case_2(self):
        # Test case when element is not present
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_case_invalid(self):
        # Test case for invalid input (empty array)
        self.assertEqual(binary_search([], 1), -1)

if __name__ == '__main__':
    unittest.main()
