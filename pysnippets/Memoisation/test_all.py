import unittest
from class_based_memoization import CombinatorialCalculator
from decorator import memoize
from factorial import FactorialCalculator
from fibonacci import FibonacciCalculator
from knapsack import KnapsackSolver, Item
from lcs import LCSSolver

class TestCombinatorialCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = CombinatorialCalculator()
    
    def test_combination_standard_cases(self):
        self.assertEqual(self.calculator.get_combination(5, 2), 10)
        self.assertEqual(self.calculator.get_combination(10, 5), 252)
        self.assertEqual(self.calculator.get_combination(0, 0), 1)
    
    def test_combination_edge_cases(self):
        self.assertEqual(self.calculator.get_combination(5, 0), 1)
        self.assertEqual(self.calculator.get_combination(5, 5), 1)
        self.assertEqual(self.calculator.get_combination(5, 6), 0)
    
    def test_combination_invalid_input(self):
        with self.assertRaises(TypeError):
            self.calculator.get_combination("5", 2)
        with self.assertRaises(TypeError):
            self.calculator.get_combination(5, "2")

class TestMemoizeDecorator(unittest.TestCase):
    
    def test_memoize_add_function(self):
        call_count = 0
        
        @memoize
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b
        
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 1)

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

class TestKnapsackSolver(unittest.TestCase):
    
    def test_knapsack_standard_case(self):
        items = (
            Item(value=60, weight=10),
            Item(value=100, weight=20),
            Item(value=120, weight=30),
        )
        self.assertEqual(KnapsackSolver.knapsack(50, items, 3), 220)
    
    def test_knapsack_no_items(self):
        items = ()
        self.assertEqual(KnapsackSolver.knapsack(50, items, 0), 0)
    
    def test_knapsack_zero_capacity(self):
        items = (
            Item(value=60, weight=10),
        )
        self.assertEqual(KnapsackSolver.knapsack(0, items, 1), 0)
    
    def test_knapsack_item_exceeds_capacity(self):
        items = (
            Item(value=100, weight=60),
        )
        self.assertEqual(KnapsackSolver.knapsack(50, items, 1), 0)

class TestLCSSolver(unittest.TestCase):
    
    def test_lcs_standard_case(self):
        self.assertEqual(LCSSolver.lcs("AGGTAB", "GXTXAYB", 6, 7), 4)
    
    def test_lcs_no_common_subsequence(self):
        self.assertEqual(LCSSolver.lcs("ABC", "DEF", 3, 3), 0)
    
    def test_lcs_empty_string(self):
        self.assertEqual(LCSSolver.lcs("", "ABC", 0, 3), 0)
        self.assertEqual(LCSSolver.lcs("ABC", "", 3, 0), 0)
    
    def test_lcs_complete_overlap(self):
        self.assertEqual(LCSSolver.lcs("ABC", "ABC", 3, 3), 3)

if __name__ == "__main__":
    unittest.main() 