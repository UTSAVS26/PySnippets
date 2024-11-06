import unittest
from list_manipulation import ListManipulator

class TestListManipulator(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(ListManipulator.remove_duplicates([1, 2, 2, 3, 4, 4]), [1, 2, 3, 4])
        self.assertEqual(ListManipulator.remove_duplicates([1, 1, 1]), [1])

    def test_flatten_nested_list(self):
        self.assertEqual(ListManipulator.flatten_nested_list([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(ListManipulator.flatten_nested_list([]), [])

    def test_list_intersection(self):
        self.assertEqual(ListManipulator.list_intersection([1, 2, 3], [2, 3, 4]), [2, 3])
        self.assertEqual(ListManipulator.list_intersection([1, 2], [3, 4]), [])

    def test_random_shuffle(self):
        shuffled = ListManipulator.random_shuffle([1, 2, 3, 4])
        self.assertEqual(sorted(shuffled), [1, 2, 3, 4])  # Check if all elements are present

    def test_sort_by_frequency(self):
        self.assertEqual(ListManipulator.sort_by_frequency([4, 5, 6, 4, 5, 4]), [4, 4, 4, 5, 5, 6])
        self.assertEqual(ListManipulator.sort_by_frequency([1, 2, 2, 3, 3, 3]), [3, 3, 3, 2, 2, 1])

if __name__ == '__main__':
    unittest.main() 