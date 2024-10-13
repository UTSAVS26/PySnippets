import unittest
from pysnippets.Sorting.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    # Add test cases for bubble sort
    def test_sort_by_age(self):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
        sorted_data = bubble_sort(data, key="age")
        expected = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
        self.assertEqual(sorted_data, expected)

    def test_empty_list(self):
        self.assertEqual(bubble_sort([], "age"), [])

    # Additional test cases for negative, float, etc.

if __name__ == "__main__":
    unittest.main()
