import unittest
from pysnippets.utilities.flatten import flatten


class TestFlatten(unittest.TestCase):

    def test_flatten_single_level(self):
        nested = [1, 2, 3]
        result = flatten(nested)
        self.assertEqual(result, [1, 2, 3])

    def test_flatten_nested_list(self):
        nested = [[1, 2], [3, [4, 5]], 6]
        result = flatten(nested)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_flatten_empty_list(self):
        nested = []
        result = flatten(nested)
        self.assertEqual(result, [])

    def test_flatten_deeply_nested(self):
        nested = [[[[1], 2], 3], 4]
        result = flatten(nested)
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
