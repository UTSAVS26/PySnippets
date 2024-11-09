import unittest
from class_based_memoization import CombinatorialCalculator

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

if __name__ == "__main__":
    unittest.main() 