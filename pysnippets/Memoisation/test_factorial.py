import unittest
from factorial import FactorialCalculator

class TestFactorialCalculator(unittest.TestCase):
    
    def test_factorial_standard_cases(self):
        self.assertEqual(FactorialCalculator.factorial(0), 1)
        self.assertEqual(FactorialCalculator.factorial(1), 1)
        self.assertEqual(FactorialCalculator.factorial(5), 120)
        self.assertEqual(FactorialCalculator.factorial(10), 3628800)
    
    def test_factorial_invalid_input(self):
        with self.assertRaises(ValueError):
            FactorialCalculator.factorial(-1)
        with self.assertRaises(ValueError):
            FactorialCalculator.factorial(-10)

if __name__ == "__main__":
    unittest.main() 