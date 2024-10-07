# test_list_manipulation.py
import unittest
from pysnippets.lists.list_manipulation import (
    add_to_list,
    remove_from_list,
    find_in_list,
    sort_list,
    merge_lists,
    unique_elements,
    list_average,
)

class TestListManipulation(unittest.TestCase):

    def test_add_to_list(self):
        lst = [1, 2, 3]
        self.assertEqual(add_to_list(lst, 4), [1, 2, 3, 4])
        self.assertEqual(add_to_list([], 1), [1])

    def test_remove_from_list(self):
        lst = [1, 2, 3, 4]
        self.assertEqual(remove_from_list(lst, 3), [1, 2, 4])
        self.assertEqual(remove_from_list(lst, 5), [1, 2, 3, 4])  # Item not in list

    def test_find_in_list(self):
        lst = [1, 2, 3, 4]
        self.assertTrue(find_in_list(lst, 3))
        self.assertFalse(find_in_list(lst, 5))

    def test_sort_list(self):
        lst = [3, 1, 4, 2]
        self.assertEqual(sort_list(lst), [1, 2, 3, 4])
        self.assertEqual(sort_list([]), [])

    def test_merge_lists(self):
        lst1 = [1, 2]
        lst2 = [3, 4]
        self.assertEqual(merge_lists(lst1, lst2), [1, 2, 3, 4])

    def test_unique_elements(self):
        lst = [1, 2, 2, 3, 4, 4]
        self.assertEqual(unique_elements(lst), [1, 2, 3, 4])

    def test_list_average(self):
        lst = [1, 2, 3, 4]
        self.assertEqual(list_average(lst), 2.5)
        self.assertEqual(list_average([]), 0)  # Edge case for empty list

if __name__ == "__main__":
    unittest.main()

