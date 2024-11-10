import unittest
from radiix_sort import radix_sort

class TestRadixSort(unittest.TestCase):
    def test_radix_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 170},
            {"name": "Bob", "age": 45},
            {"name": "Charlie", "age": 75},
            {"name": "David", "age": 150}
        ]
        expected = [
            {"name": "Bob", "age": 45},
            {"name": "Charlie", "age": 75},
            {"name": "David", "age": 150},
            {"name": "Alice", "age": 170}
        ]
        result = radix_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_radix_sort_empty(self):
        data = []
        expected = []
        result = radix_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_radix_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 30}]
        with self.assertRaises(KeyError):
            radix_sort(data, key="height")

    def test_radix_sort_non_integer_key(self):
        data = [{"name": "Alice", "age": "thirty"}]
        with self.assertRaises(ValueError):
            radix_sort(data, key="age")

    def test_radix_sort_negative_key(self):
        data = [{"name": "Alice", "age": -10}]
        with self.assertRaises(ValueError):
            radix_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 