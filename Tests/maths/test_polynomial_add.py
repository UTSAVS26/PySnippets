import unittest
from pysnippets.math.polynomial_add import Polynomial, add_polynomials

class TestPolynomialOperations(unittest.TestCase):

    def test_add_polynomials(self):
        # Create first polynomial
        poly1 = Polynomial()
        poly1.add_term(3, 2)  # 3x^2
        poly1.add_term(5, 1)  # 5x
        poly1.add_term(9, 3)  # 9x^3

        # Create second polynomial
        poly2 = Polynomial()
        poly2.add_term(2, 2)  # 2x^2
        poly2.add_term(-5, 1) # -5x
        poly2.add_term(1, 3)  # 1x^3
        poly2.add_term(1, 4)  # 1x^4

        # Add the polynomials together
        added_poly = add_polynomials([poly1, poly2])
        

        # Verify the result
        self.assertEqual(added_poly.display(), "1x^4 + 10x^3 + 5x^2")

    def test_add_empty_polynomials(self):
        # Test case with empty polynomials
        poly1 = Polynomial()
        poly2 = Polynomial()

        # Add empty polynomials
        added_poly = add_polynomials([poly1, poly2])

        # Verify result is "0"
        self.assertEqual(added_poly.display(), "0")

    def test_single_polynomial(self):
        # Test case with a single polynomial
        poly = Polynomial()
        poly.add_term(3, 2)  # 3x^2

        # Add a single polynomial
        added_poly = add_polynomials([poly])

        # Verify result
        self.assertEqual(added_poly.display(), "3x^2")

if __name__ == '__main__':
    unittest.main()

