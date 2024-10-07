# test_dictionary_manipulation.py
import unittest
from pysnippets.dictionaries.dictionary_manipulation import (
    add_key_value,
    remove_key,
    find_value,
    merge_dictionaries,
    unique_values,
    count_key_occurrences,
)

class TestDictionaryManipulation(unittest.TestCase):

    def test_add_key_value(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(add_key_value(d, 'c', 3), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(add_key_value({}, 'x', 5), {'x': 5})

    def test_remove_key(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(remove_key(d, 'b'), {'a': 1, 'c': 3})
        self.assertEqual(remove_key(d, 'x'), d)  # Key not in dict

    def test_find_value(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertTrue(find_value(d, 2))
        self.assertFalse(find_value(d, 5))

    def test_merge_dictionaries(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'b': 3, 'c': 4}
        self.assertEqual(merge_dictionaries(d1, d2), {'a': 1, 'b': 3, 'c': 4})

    def test_unique_values(self):
        d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
        self.assertEqual(unique_values(d), [1, 2, 3])

    def test_count_key_occurrences(self):
        d = {'a': 1, 'b': 2, 'a': 3}  # 'a' is repeated
        self.assertEqual(count_key_occurrences(d, 'a'), 1)  # Python dict keys are unique

if __name__ == "__main__":
    unittest.main()

