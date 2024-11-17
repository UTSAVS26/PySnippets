import unittest
from pysnippets.Sorting.cocktail_sort import cocktail_sort

class TestCocktailSort(unittest.TestCase):
    def test_cocktail_sort_ascending(self):
        data = [
            {"name": "Alice", "age": 45},
            {"name": "Bob", "age": 22},
            {"name": "Charlie", "age": 33},
            {"name": "David", "age": 27}
        ]
        expected = [
            {"name": "Bob", "age": 22},
            {"name": "David", "age": 27},
            {"name": "Charlie", "age": 33},
            {"name": "Alice", "age": 45}
        ]
        result = cocktail_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_cocktail_sort_descending(self):
        data = [
            {"name": "Alice", "age": 45},
            {"name": "Bob", "age": 22},
            {"name": "Charlie", "age": 33},
            {"name": "David", "age": 27}
        ]
        expected = [
            {"name": "Alice", "age": 45},
            {"name": "Charlie", "age": 33},
            {"name": "David", "age": 27},
            {"name": "Bob", "age": 22}
        ]
        result = cocktail_sort(data, key="age", reverse=True)
        self.assertEqual(result, expected)

    def test_cocktail_sort_empty(self):
        data = []
        expected = []
        result = cocktail_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_cocktail_sort_invalid_key(self):
        data = [{"name": "Alice", "age": 45}]
        with self.assertRaises(KeyError):
            cocktail_sort(data, key="height")

    def test_cocktail_sort_non_dict_input(self):
        data = ["Alice", "Bob", "Charlie"]
        with self.assertRaises(TypeError):
            cocktail_sort(data, key="age")

    def test_cocktail_sort_missing_key(self):
        data = [{"name": "Alice", "age": 45}, {"name": "Bob"}]
        with self.assertRaises(KeyError):
            cocktail_sort(data, key="age")

    def test_cocktail_sort_mixed_key_types(self):
        data = [
            {"name": "Alice", "age": 45},
            {"name": "Bob", "age": "22"},  # Age is a string here
            {"name": "Charlie", "age": 33}
        ]
        with self.assertRaises(TypeError):
            cocktail_sort(data, key="age")

    def test_cocktail_sort_duplicate_keys(self):
        data = [
            {"name": "Alice", "age": 33},
            {"name": "Bob", "age": 33},
            {"name": "Charlie", "age": 45},
            {"name": "David", "age": 22}
        ]
        expected = [
            {"name": "David", "age": 22},
            {"name": "Alice", "age": 33},
            {"name": "Bob", "age": 33},
            {"name": "Charlie", "age": 45}
        ]
        result = cocktail_sort(data, key="age")
        self.assertEqual(result, expected)

    def test_cocktail_sort_invalid_key_type(self):
        data = [
            {"name": "Alice", "age": 45},
            {"name": "Bob", "age": 22}
        ]
        with self.assertRaises(TypeError):
            cocktail_sort(data, key=123)


if __name__ == "__main__":
    unittest.main() 