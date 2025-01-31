import unittest
import sympy as sp
import numpy as np
from jacobian import symbolic_jacobian, numerical_jacobian

class TestJacobianFunctions(unittest.TestCase):

    def test_symbolic_jacobian(self):
        # Test symbolic Jacobian
        x, y = sp.symbols('x y')
        funcs = [x**2 + y**2, sp.sin(x) * sp.cos(y)]
        vars = [x, y]
        jacobian_sym = symbolic_jacobian(funcs, vars)
        expected_jacobian = sp.Matrix([[2*x, 2*y], [sp.cos(x)*sp.cos(y), -sp.sin(x)*sp.sin(y)]])
        print("Symbolic Jacobian:", jacobian_sym)
        self.assertTrue(jacobian_sym.equals(expected_jacobian))

        # Additional symbolic example
        u, v = sp.symbols('u v')
        funcs2 = [u**3 + v**3, sp.exp(u) * sp.log(v)]
        vars2 = [u, v]
        jacobian_sym2 = symbolic_jacobian(funcs2, vars2)
        expected_jacobian2 = sp.Matrix([[3*u**2, 3*v**2], [sp.exp(u)*sp.log(v), sp.exp(u)/v]])
        print("Additional Symbolic Jacobian:", jacobian_sym2)
        self.assertTrue(jacobian_sym2.equals(expected_jacobian2))

    def test_numerical_jacobian(self):
        # Test numerical Jacobian
        def example_func(point):
            x, y = point
            return np.array([x**2 + y**2, np.sin(x) * np.cos(y)])

        point = np.array([1.0, 2.0])
        jacobian_num = numerical_jacobian(example_func, point)
        expected_jacobian = np.array([[2.0, 4.0], [-0.22484, -0.76515]])
        print("Numerical Jacobian at point [1.0, 2.0]:", jacobian_num)
        np.testing.assert_almost_equal(jacobian_num, expected_jacobian, decimal=5)

        # Additional numerical example
        def example_func2(point):
            u, v = point
            return np.array([u**3 + v**3, np.exp(u) * np.log(v)])

        point2 = np.array([1.0, 2.0])
        jacobian_num2 = numerical_jacobian(example_func2, point2)
        expected_jacobian2 = np.array([[3.0, 12.0], [np.exp(1.0) * np.log(2.0), np.exp(1.0) / 2.0]])
        print("Numerical Jacobian at point [1.0, 2.0] for additional example:", jacobian_num2)
        np.testing.assert_almost_equal(jacobian_num2, expected_jacobian2, decimal=5)

if __name__ == '__main__':
    unittest.main()