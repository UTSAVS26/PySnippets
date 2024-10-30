
import unittest
from dictionarywithlru import fibonacci

class TestFibonacciMemoization(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

if __name__ == '__main__':
    unittest.main()
