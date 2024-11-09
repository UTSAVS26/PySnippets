import unittest
from fibonacci import FibonacciCalculator

class TestFibonacciCalculator(unittest.TestCase):
    
    def test_fibonacci_standard_cases(self):
        self.assertEqual(FibonacciCalculator.fibonacci(1), 1)
        self.assertEqual(FibonacciCalculator.fibonacci(5), 5)
        self.assertEqual(FibonacciCalculator.fibonacci(10), 55)
    
    def test_fibonacci_invalid_input(self):
        with self.assertRaises(ValueError):
            FibonacciCalculator.fibonacci(0)
        with self.assertRaises(ValueError):
            FibonacciCalculator.fibonacci(-5)

if __name__ == "__main__":
    unittest.main() 