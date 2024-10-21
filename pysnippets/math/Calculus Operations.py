# Calculus Operations Module: calculus_operations.py

import sympy as sp

# Define a symbolic variable
x = sp.symbols('x')

def derivative(expr, var):
    """Returns the derivative of expr with respect to var."""
    return sp.diff(expr, var)

def definite_integral(expr, var, a, b):
    """Returns the definite integral of expr from a to b with respect to var."""
    return sp.integrate(expr, (var, a, b))

def limit_of_function(expr, var, point):
    """Returns the limit of expr as var approaches point."""
    return sp.limit(expr, var, point)

def taylor_series(expr, var, point, n):
    """Returns the Taylor series expansion of expr at point up to order n."""
    return sp.series(expr, var, point, n).removeO()

# Example usage
if __name__ == "__main__":
    expr = x**2 + 3*x + 2
    print("Derivative:", derivative(expr, x))
    print("Definite Integral (from 0 to 1):", definite_integral(expr, x, 0, 1))
    print("Limit as x -> 0:", limit_of_function(expr, x, 0))
    print("Taylor Series Expansion:", taylor_series(sp.sin(x), x, 0, 5))
