import unittest
from pysnippets.Sorting.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_array(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_mixed_array(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_duplicates(self):
        self.assertEqual(selection_sort([3, 1, 2, 3, 2]), [1, 2, 2, 3, 3])

    def test_single_element(self):
        self.assertEqual(selection_sort([10]), [10])

    def test_empty_array(self):
        self.assertEqual(selection_sort([]), [])

if __name__ == "__main__":
    unittest.main()
