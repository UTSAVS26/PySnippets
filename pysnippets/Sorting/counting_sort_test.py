import unittest
from counting_sort import counting_sort

class TestCountingSort(unittest.TestCase):
    def test_counting_sort_ascending(self):
        data = [
            {"name": "Alice", "score": 88},
            {"name": "Bob", "score": 75},
            {"name": "Charlie", "score": 93},
            {"name": "David", "score": 85},
            {"name": "Eve", "score": 77}
        ]
        expected = [
            {"name": "Bob", "score": 75},
            {"name": "Eve", "score": 77},
            {"name": "David", "score": 85},
            {"name": "Alice", "score": 88},
            {"name": "Charlie", "score": 93}
        ]
        result = counting_sort(data, key="score")
        self.assertEqual(result, expected)

    def test_counting_sort_descending(self):
        data = [
            {"name": "Alice", "score": 88},
            {"name": "Bob", "score": 75},
            {"name": "Charlie", "score": 93},
            {"name": "David", "score": 85},
            {"name": "Eve", "score": 77}
        ]
        expected = [
            {"name": "Charlie", "score": 93},
            {"name": "Alice", "score": 88},
            {"name": "David", "score": 85},
            {"name": "Eve", "score": 77},
            {"name": "Bob", "score": 75}
        ]
        result = counting_sort(data, key="score", reverse=True)
        self.assertEqual(result, expected)

    def test_counting_sort_empty(self):
        data = []
        expected = []
        result = counting_sort(data, key="score")
        self.assertEqual(result, expected)

    def test_counting_sort_invalid_key(self):
        data = [{"name": "Alice", "score": 88}]
        with self.assertRaises(KeyError):
            counting_sort(data, key="grade")

    def test_counting_sort_non_integer_key(self):
        data = [{"name": "Alice", "score": "eighty-eight"}]
        with self.assertRaises(ValueError):
            counting_sort(data, key="score")

    def test_counting_sort_negative_key(self):
        data = [{"name": "Alice", "score": -10}]
        with self.assertRaises(ValueError):
            counting_sort(data, key="score")

if __name__ == "__main__":
    unittest.main() 