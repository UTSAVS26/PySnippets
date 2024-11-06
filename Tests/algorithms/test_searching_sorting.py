import unittest
from searching_sorting import linear_search, binary_search, jump_search, exponential_search
from searching_sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort, counting_sort, radix_sort

class TestAlgorithms(unittest.TestCase):

    # Searching Algorithms Test Cases

    def test_linear_search(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(linear_search(arr, 9), 2)
        self.assertEqual(linear_search(arr, 10), -1)

    def test_binary_search(self):
        arr = [1, 2, 5, 5, 6, 9]
        self.assertEqual(binary_search(arr, 9), 5)
        self.assertEqual(binary_search(arr, 10), -1)

    def test_jump_search(self):
        arr = [1, 2, 5, 5, 6, 9]
        self.assertEqual(jump_search(arr, 9), 5)
        self.assertEqual(jump_search(arr, 10), -1)

    def test_exponential_search(self):
        arr = [1, 2, 5, 5, 6, 9]
        self.assertEqual(exponential_search(arr, 9), 5)
        self.assertEqual(exponential_search(arr, 10), -1)

    # Sorting Algorithms Test Cases

    def test_bubble_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(bubble_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_selection_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(selection_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_insertion_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(insertion_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_merge_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(merge_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_quick_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(quick_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_heap_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(heap_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_counting_sort(self):
        arr = [5, 2, 9, 1, 5, 6]
        self.assertEqual(counting_sort(arr), [1, 2, 5, 5, 6, 9])

    def test_radix_sort(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        self.assertEqual(radix_sort(arr), [2, 24, 45, 66, 75, 90, 170, 802])


if __name__ == "__main__":
    unittest.main()
