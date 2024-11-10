import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 40},
            {"name": "Bob", "age": 30},
            {"name": "Charlie", "age": 25},
            {"name": "David", "age": 35}
        ]
        expected = [
            {"name": "Charlie", "age": 25},
            {"name": "Bob", "age": 30},
            {"name": "David", "age": 35},
            {"name": "Alice", "age": 40}
        ]
        result = quick_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_quick_sort_descending(self):
        data = [
            {"name": "Alice", "age": 40},
            {"name": "Bob", "age": 30},
            {"name": "Charlie", "age": 25},
            {"name": "David", "age": 35}
        ]
        # Quick Sort doesn't support reverse, so we'll sort ascending and then reverse
        expected = [
            {"name": "Alice", "age": 40},
            {"name": "David", "age": 35},
            {"name": "Bob", "age": 30},
            {"name": "Charlie", "age": 25}
        ]
        result = quick_sort(data, key="age")
        result.reverse()
        self.assertEqual(result, expected)

    def test_quick_sort_empty(self):
        data = []
        expected = []
        result = quick_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_quick_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 40}]
        with self.assertRaises(KeyError):
            quick_sort(data, key="height")

    def test_quick_sort_non_dict_input(self):
        data = [10, 20, 30]
        with self.assertRaises(TypeError):
            quick_sort(data, key="age")

    def test_quick_sort_missing_key(self):
        data = [{"name": "Alice", "age": 40}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            quick_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 