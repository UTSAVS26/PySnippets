import unittest
from pysnippets.Sorting.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    # Add test cases for merge sort
    def test_sort_by_age(self):
        data = [{"name": "Charlie", "age": 35}, {"name": "Alice", "age": 30}]
        sorted_data = merge_sort(data, key="age")
        expected = [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 35}]
        self.assertEqual(sorted_data, expected)

    # Additional test cases for negative, float, etc.

if __name__ == "__main__":
    unittest.main()
