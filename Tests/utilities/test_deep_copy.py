
import unittest
from deep_copy import deep_copy

class TestDeepCopy(unittest.TestCase):
    def test_deep_copy(self):
        original = {'a': 1, 'b': [2, 3, 4]}
        copy = deep_copy(original)
        self.assertEqual(copy, original)
        self.assertIsNot(copy, original)

if __name__ == '__main__':
    unittest.main()
