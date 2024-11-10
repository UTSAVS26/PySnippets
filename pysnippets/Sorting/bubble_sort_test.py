import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
            {"name": "David", "age": 20}
        ]
        expected = [
            {"name": "David", "age": 20},
            {"name": "Bob", "age": 25},
            {"name": "Alice", "age": 30},
            {"name": "Charlie", "age": 35}
        ]
        result = bubble_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_bubble_sort_descending(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
            {"name": "David", "age": 20}
        ]
        expected = [
            {"name": "Charlie", "age": 35},
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "David", "age": 20}
        ]
        result = bubble_sort(data, key="age", reverse=True)
        self.assertEqual(result, expected)

    def test_bubble_sort_empty(self):
        data = []
        expected = []
        result = bubble_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_bubble_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 30}]
        with self.assertRaises(KeyError):
            bubble_sort(data, key="height")

    def test_bubble_sort_non_dict_input(self):
        data = [1, 2, 3]
        with self.assertRaises(TypeError):
            bubble_sort(data, key="age")

    def test_bubble_sort_missing_key(self):
        data = [{"name": "Alice", "age": 30}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            bubble_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 