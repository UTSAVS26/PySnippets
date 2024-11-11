import unittest
from complex_number import ComplexNumber
from exceptions import DivisionByZeroError

class TestComplexNumber(unittest.TestCase):
    
    def setUp(self):
        self.c1 = ComplexNumber(1, 2)
        self.c2 = ComplexNumber(3, 4)

    def test_division(self):
        result = self.c1.divide(self.c2)
        self.assertAlmostEqual(result.real, 0.44)
        self.assertAlmostEqual(result.imaginary, 0.08)

    def test_division_by_zero(self):
        c_zero = ComplexNumber(0, 0)
        with self.assertRaises(DivisionByZeroError):
            self.c1.divide(c_zero)

if   __name__ == '__main__':
    unittest.main()