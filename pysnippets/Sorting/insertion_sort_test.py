import unittest
from insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 34},
            {"name": "Bob", "age": 23},
            {"name": "Charlie", "age": 45},
            {"name": "David", "age": 29}
        ]
        expected = [
            {"name": "Bob", "age": 23},
            {"name": "David", "age": 29},
            {"name": "Alice", "age": 34},
            {"name": "Charlie", "age": 45}
        ]
        result = insertion_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_insertion_sort_descending(self):
        data = [
            {"name": "Alice", "age": 34},
            {"name": "Bob", "age": 23},
            {"name": "Charlie", "age": 45},
            {"name": "David", "age": 29}
        ]
        expected = [
            {"name": "Charlie", "age": 45},
            {"name": "Alice", "age": 34},
            {"name": "David", "age": 29},
            {"name": "Bob", "age": 23}
        ]
        result = insertion_sort(data, key="age", reverse=True)
        self.assertEqual(result, expected)

    def test_insertion_sort_empty(self):
        data = []
        expected = []
        result = insertion_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_insertion_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 34}]
        with self.assertRaises(KeyError):
            insertion_sort(data, key="height")

    def test_insertion_sort_non_dict_input(self):
        data = [10, 20, 30]
        with self.assertRaises(TypeError):
            insertion_sort(data, key="age")

    def test_insertion_sort_missing_key(self):
        data = [{"name": "Alice", "age": 34}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            insertion_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 