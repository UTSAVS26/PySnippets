import unittest
from pysnippets.Sorting.cocktail_sort import cocktail_sort

class TestCocktailSort(unittest.TestCase):
    # Test case for basic sorting by age
    def test_sort_by_age(self):
        data = [{"name": "Charlie", "age": 35},{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        sorted_data = cocktail_sort(data, key="age")
        expected = [{"name": "Bob", "age": 25},{"name": "Alice", "age": 30},{"name": "Charlie", "age": 35},]
        self.assertEqual(sorted_data, expected)

    # Test case for sorting by age (descending)
    def test_sort_by_age_descending(self):
        data = [{"name": "Charlie", "age": 35},{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        sorted_data = cocktail_sort(data, key="age", reverse=True)
        expected = [{"name": "Charlie", "age": 35},{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        self.assertEqual(sorted_data, expected)

    # Test case for sorting by name (ascending)
    def test_sort_by_name(self):
        data = [{"name": "Charlie", "age": 35},{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        sorted_data = cocktail_sort(data, key="name")
        expected = [{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},{"name": "Charlie", "age": 35},]
        self.assertEqual(sorted_data, expected)

    # Test case for sorting by name (descending)
    def test_sort_by_name_descending(self):
        data = [{"name": "Charlie", "age": 35},{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        sorted_data = cocktail_sort(data, key="name", reverse=True)
        expected = [{"name": "Charlie", "age": 35},{"name": "Bob", "age": 25},{"name": "Alice", "age": 30},]
        self.assertEqual(sorted_data, expected)

    # Test case for empty list
    def test_empty_list(self):
        data = []
        sorted_data = cocktail_sort(data, key="age")
        expected = []
        self.assertEqual(sorted_data, expected)

    # Test case for single element list
    def test_single_element_list(self):
        data = [{"name": "Alice", "age": 30}]
        sorted_data = cocktail_sort(data, key="age")
        expected = [{"name": "Alice", "age": 30}]
        self.assertEqual(sorted_data, expected)

    # Test case for multiple elements with same age
    def test_same_age(self):
        data = [{"name": "Alice", "age": 30},{"name": "Bob", "age": 30},{"name": "Charlie", "age": 30}, ]
        sorted_data = cocktail_sort(data, key="age")
        expected = [{"name": "Alice", "age": 30},{"name": "Bob", "age": 30},{"name": "Charlie", "age": 30},]
        self.assertEqual(sorted_data, expected)

    # Test case for sorting a mixed list by age
    def test_mixed_list(self):
        data = [ {"name": "Eve", "age": 22},{"name": "Dan", "age": 28},{"name": "Charlie", "age": 35},{"name": "Bob", "age": 25},{"name": "Alice", "age": 30},]
        sorted_data = cocktail_sort(data, key="age")
        expected = [{"name": "Eve", "age": 22},{"name": "Bob", "age": 25},{"name": "Dan", "age": 28},{"name": "Alice", "age": 30},{"name": "Charlie", "age": 35},]
        self.assertEqual(sorted_data, expected)

    # Test case for invalid key
    def test_invalid_key(self):
        data = [{"name": "Alice", "age": 30},{"name": "Bob", "age": 25},]
        with self.assertRaises(KeyError):
            cocktail_sort(data, key="height")

if __name__ == "__main__":
    unittest.main()
