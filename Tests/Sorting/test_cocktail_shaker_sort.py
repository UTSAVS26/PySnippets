import unittest
from pysnippets.Sorting.cocktail_shaker_sort import cocktail_shaker_sort  

class TestCocktailShakerSort(unittest.TestCase):
    # Test sorted list
    def test_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        sorted_data = cocktail_shaker_sort(data)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(sorted_data, expected)

    # Test reverse sorted list
    def test_reverse_sorted_list(self):
        data = [5, 4, 3, 2, 1]
        sorted_data = cocktail_shaker_sort(data)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(sorted_data, expected)

    # Test unsorted list
    def test_unsorted_list(self):
        data = [5, 3, 8, 4, 2]
        sorted_data = cocktail_shaker_sort(data)
        expected = [2, 3, 4, 5, 8]
        self.assertEqual(sorted_data, expected)

    # Test single element list
    def test_single_element_list(self):
        data = [42]
        sorted_data = cocktail_shaker_sort(data)
        expected = [42]
        self.assertEqual(sorted_data, expected)

    # Test empty list
    def test_empty_list(self):
        data = []
        sorted_data = cocktail_shaker_sort(data)
        expected = []
        self.assertEqual(sorted_data, expected)

    # Test floats and negatives
    def test_floats_and_negatives(self):
        data = [3.5, 2.1, -1, 0, 5.5]
        sorted_data = cocktail_shaker_sort(data)
        expected = [-1, 0, 2.1, 3.5, 5.5]
        self.assertEqual(sorted_data, expected)

    # Test duplicates
    def test_duplicates(self):
        data = [4, 2, 3, 4, 1, 4]
        sorted_data = cocktail_shaker_sort(data)
        expected = [1, 2, 3, 4, 4, 4]
        self.assertEqual(sorted_data, expected)

    # Test large numbers
    def test_large_numbers(self):
        data = [1000000, 500, 250, 999999, 1]
        sorted_data = cocktail_shaker_sort(data)
        expected = [1, 250, 500, 999999, 1000000]
        self.assertEqual(sorted_data, expected)

if __name__ == "__main__":
    unittest.main()