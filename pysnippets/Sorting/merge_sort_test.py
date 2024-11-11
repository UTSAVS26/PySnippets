import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_merge_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 28},
            {"name": "Bob", "age": 19},
            {"name": "Charlie", "age": 24},
            {"name": "David", "age": 22}
        ]
        expected = [
            {"name": "Bob", "age": 19},
            {"name": "David", "age": 22},
            {"name": "Charlie", "age": 24},
            {"name": "Alice", "age": 28}
        ]
        result = merge_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_merge_sort_descending(self):
        data = [
            {"name": "Alice", "age": 28},
            {"name": "Bob", "age": 19},
            {"name": "Charlie", "age": 24},
            {"name": "David", "age": 22}
        ]
        # Since merge_sort doesn't have a reverse parameter, we'll reverse the result manually
        expected = [
            {"name": "Alice", "age": 28},
            {"name": "Charlie", "age": 24},
            {"name": "David", "age": 22},
            {"name": "Bob", "age": 19}
        ]
        result = merge_sort(data, key="age")
        result.reverse()
        self.assertEqual(result, expected)

    def test_merge_sort_empty(self):
        data = []
        expected = []
        result = merge_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_merge_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 28}]
        with self.assertRaises(KeyError):
            merge_sort(data, key="height")

    def test_merge_sort_non_dict_input(self):
        data = ["alice", "bob", "charlie"]
        with self.assertRaises(TypeError):
            merge_sort(data, key="age")

    def test_merge_sort_missing_key(self):
        data = [{"name": "Alice", "age": 28}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            merge_sort(data, key="age")

if __name__ == "__main__":
    unittest.main() 