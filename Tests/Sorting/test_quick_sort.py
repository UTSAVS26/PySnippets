import unittest
from pysnippets.Sorting.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    # Add test cases for quick sort
    def test_sort_by_age(self):
        data = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
        sorted_data = quick_sort(data, key="age")
        expected = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
        self.assertEqual(sorted_data, expected)

    # Additional test cases for negative, float, etc.

if __name__ == "__main__":
    unittest.main()
