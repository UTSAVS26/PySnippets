
import unittest
from flatten import flatten_list

class TestFlattenList(unittest.TestCase):
    def test_flatten_list(self):
        nested_list = [1, [2, [3, 4], 5], 6]
        self.assertEqual(flatten_list(nested_list), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
