import unittest
from pysnippets.maths.pascals_triangle import pascals_triangle, get_pascals_triangle_row, binomial_coefficient, sum_pascals_triangle_row, factorial, polynomial_expansion, pascals_triangle_modulo

class TestPascalsTriangle(unittest.TestCase):
    
    def test_pascals_triangle(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        self.assertEqual(pascals_triangle(5), expected)
        
    def test_get_pascals_triangle_row(self):
        self.assertEqual(get_pascals_triangle_row(4), [1, 4, 6, 4, 1])
    
    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coefficient(5, 2), 10)
        
    def test_sum_pascals_triangle_row(self):
        self.assertEqual(sum_pascals_triangle_row(4), 16)
        
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        
    def test_polynomial_expansion(self):
        expected = "1*2^4*3^0 + 4*2^3*3^1 + 6*2^2*3^2 + 4*2^1*3^3 + 1*2^0*3^4"
        self.assertEqual(polynomial_expansion(2, 3, 4), expected)
        
    def test_pascals_triangle_modulo(self):
        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1, 1]
        ]
        self.assertEqual(pascals_triangle_modulo(5, 3), expected)

if __name__ == "__main__":
    unittest.main()