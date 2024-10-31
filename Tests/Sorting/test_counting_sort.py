import unittest
from pysnippets.Sorting.counting_sort import counting_sort


class TestCountingSort(unittest.TestCase):
    def test_sorted_array(self):
        arr = [4, 2, 2, 8, 3, 3, 1]
        expected_result = [1, 2, 2, 3, 3, 4, 8]
        self.assertEqual(counting_sort(arr), expected_result)

    def test_empty_array(self):
        arr = []
        expected_result = []
        self.assertEqual(counting_sort(arr), expected_result)

    def test_single_element_array(self):
        arr = [5]
        expected_result = [5]
        self.assertEqual(counting_sort(arr), expected_result)

    def test_already_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(counting_sort(arr), expected_result)

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(counting_sort(arr), expected_result)

    def test_large_numbers(self):
        arr = [1000, 500, 100, 1000, 0]
        expected_result = [0, 100, 500, 1000, 1000]
        self.assertEqual(counting_sort(arr), expected_result)


if __name__ == "__main__":
    unittest.main()
