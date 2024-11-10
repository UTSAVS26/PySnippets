import unittest
from cocktail_shaker_sort import cocktail_shaker_sort

class TestCocktailShakerSort(unittest.TestCase):
    def test_cocktail_shaker_sort_ascending(self):
        data = [5, 3, 8, 4, 2]
        expected = [2, 3, 4, 5, 8]
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

    def test_cocktail_shaker_sort_descending(self):
        data = [5, 3, 8, 4, 2]
        expected = [8, 5, 4, 3, 2]
        sorted_data = cocktail_shaker_sort(data)
        sorted_data.reverse()
        self.assertEqual(sorted_data, expected)

    def test_cocktail_shaker_sort_empty(self):
        data = []
        expected = []
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

    def test_cocktail_shaker_sort_single_element(self):
        data = [1]
        expected = [1]
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

    def test_cocktail_shaker_sort_already_sorted(self):
        data = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

    def test_cocktail_shaker_sort_reverse_sorted(self):
        data = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

    def test_cocktail_shaker_sort_with_duplicates(self):
        data = [4, 2, 5, 2, 3, 4]
        expected = [2, 2, 3, 4, 4, 5]
        result = cocktail_shaker_sort(data)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main() 