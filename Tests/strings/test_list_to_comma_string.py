# test_list_to_comma_string.py

import unittest
from pysnippets.strings.list_to_comma_string import list_to_comma_string


class TestListToCommaString(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(
            list_to_comma_string(["apple", "banana", "cherry"]), "apple, banana, cherry"
        )

    def test_empty_list(self):
        self.assertEqual(list_to_comma_string([]), "")

    def test_single_item(self):
        self.assertEqual(list_to_comma_string(["apple"]), "apple")

    def test_non_string_item(self):
        with self.assertRaises(ValueError):
            list_to_comma_string(["apple", 123, "cherry"])


if __name__ == "__main__":
    unittest.main()
