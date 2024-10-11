import unittest
from pysnippets.Sorting.sort_dict_list import sort_dict_list


class TestSortDictList(unittest.TestCase):

    def test_sort_by_age_ascending(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
        ]
        sorted_data = sort_dict_list(data, key="age")
        expected = [
            {"name": "Bob", "age": 25},
            {"name": "Alice", "age": 30},
            {"name": "Charlie", "age": 35},
        ]
        self.assertEqual(sorted_data, expected)

    def test_sort_by_name_descending(self):
        data = [
            {"name": "Alice", "age": 30},
            {"name": "Bob", "age": 25},
            {"name": "Charlie", "age": 35},
        ]
        sorted_data = sort_dict_list(data, key="name", reverse=True)
        expected = [
            {"name": "Charlie", "age": 35},
            {"name": "Bob", "age": 25},
            {"name": "Alice", "age": 30},
        ]
        self.assertEqual(sorted_data, expected)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            sort_dict_list([], "key")

    def test_key_not_present(self):
        data = [{"name": "Alice"}, {"name": "Bob", "age": 25}]
        with self.assertRaises(ValueError):
            sort_dict_list(data, key="age")


if __name__ == "__main__":
    unittest.main()
