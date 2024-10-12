# test_dictionary_manipulation.py
import unittest
from pysnippets.dictionaries.dictionary_manipulation import (
    add_item,
    update_item,
    remove_item,
    check_for_key,
    iterate_keys,
    iterate_values,
    merge_dictionaries,
    copy_dictionary,
    clear_dictionary,
)

class TestDictionaryManipulation(unittest.TestCase):

    def test_add_item(self):
        d = {'a': 1}
        self.assertEqual(add_item(d, 'b', 2), {'a': 1, 'b': 2})
        self.assertEqual(add_item({}, 'key', 'value'), {'key': 'value'})

    def test_update_item(self):
        d = {'a': 1}
        self.assertEqual(update_item(d, 'a', 2), {'a': 2})
        self.assertEqual(update_item(d, 'b', 3), {'a': 1})  # Key does not exist

    def test_remove_item(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(remove_item(d, 'a'), {'b': 2})
        self.assertEqual(remove_item(d, 'c'), {'a': 1, 'b': 2})  # Key does not exist

    def test_check_for_key(self):
        d = {'a': 1}
        self.assertTrue(check_for_key(d, 'a'))
        self.assertFalse(check_for_key(d, 'b'))

    def test_iterate_keys(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(iterate_keys(d), ['a', 'b'])

    def test_iterate_values(self):
        d = {'a': 1, 'b': 2}
        self.assertEqual(iterate_values(d), [1, 2])

    def test_merge_dictionaries(self):
        d1 = {'a': 1}
        d2 = {'b': 2}
        self.assertEqual(merge_dictionaries(d1, d2), {'a': 1, 'b': 2})
        self.assertEqual(merge_dictionaries(d1, {'a': 3}), {'a': 3})  # Overwrite existing key

    def test_copy_dictionary(self):
        d = {'a': 1}
        self.assertEqual(copy_dictionary(d), {'a': 1})

    def test_clear_dictionary(self):
        d = {'a': 1}
        self.assertEqual(clear_dictionary(d), {})
        self.assertEqual(clear_dictionary({}), {})  # Clearing an already empty dictionary

if __name__ == "__main__":
    unittest.main()

