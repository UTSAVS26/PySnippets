import unittest
from pysnippets.algorithms.fibonacci import fibonacci  

class TestFibonacci(unittest.TestCase):

    def test_basic_case(self):
        # Test case for basic Fibonacci numbers
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_large_input(self):
        # Test case for larger input
        self.assertEqual(fibonacci(10), 55)

    def test_negative_input(self):
        # Test case for negative input
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()
