import unittest
from heap_sort import heap_sort

class TestHeapSort(unittest.TestCase):
    def test_heap_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 50},
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 40},
            {"name": "David", "age": 30}
        ]
        expected = [
            {"name": "Bob", "age": 20},
            {"name": "David", "age": 30},
            {"name": "Charlie", "age": 40},
            {"name": "Alice", "age": 50}
        ]
        result = heap_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_heap_sort_descending(self):
        data = [
            {"name": "Alice", "age": 50},
            {"name": "Bob", "age": 20},
            {"name": "Charlie", "age": 40},
            {"name": "David", "age": 30}
        ]
        expected = [
            {"name": "Alice", "age": 50},
            {"name": "Charlie", "age": 40},
            {"name": "David", "age": 30},
            {"name": "Bob", "age": 20}
        ]
        result = heap_sort(data, key="age", reverse=True)
        self.assertEqual(result, expected)

    def test_heap_sort_empty(self):
        data = []
        expected = []
        result = heap_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_heap_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 50}]
        with self.assertRaises(KeyError):
            heap_sort(data, key="height")

    def test_heap_sort_non_dict_input(self):
        data = [100, 50, 200]
        with self.assertRaises(TypeError):
            heap_sort(data, key="age")

    def test_heap_sort_missing_key(self):
        data = [{"name": "Alice", "age": 50}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            heap_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 