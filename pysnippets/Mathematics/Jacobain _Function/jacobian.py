import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def symbolic_jacobian(funcs, vars):
    """
    Compute the symbolic Jacobain matrix
    args:
        funcs: list of symbolic functions
        vars: list of sympy variables
    return:
        Sympy Matrix: The Jacobian matrix
    """
    jacobian_matrix = sp.Matrix(funcs).jacobian(vars)
    return jacobian_matrix

def numerical_jacobian(func, x, eps=1e-6):
    """ 
    Compute the numerical Jacobian matrix using finite differences
    Args:
        func: Callable function, takes an input vector and returns an output vector
        x: Point at which to evaluate the Jacobian (numpy array)
        eps: Small perturbation for finite differences
    Returns:
        numpy array: The Jacobian matrix
    """
    
    n = len(x)
    fx = func(x)
    m = len(fx)
    jacobian_matrix = np.zeros((m, n))
    for i in range(n):
        x_perturbed = x.copy()       
        x_perturbed[i] += eps
        jacobian_matrix[:, i] = (func(x_perturbed) - fx) / eps
    return jacobian_matrix

def plot_jacobian(func, x_range, y_range, resolution=20):
    """ 
    Plot the jacobian determinant on a grid
    Args:
        func: Callable function mapping R^2 -> R^2.
        x_range: Tuple defining the x-range (min, max).
        y_range: Tuple defining the y-range (min, max).
        resolution: Number of points per dimension.
    """
    
    x = np.linspace(x_range[0], x_range[1], resolution)
    y = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x, y)
    det_jacobain = np.zeros_like(X)
    
    def wrapper(point):
        return np.array(func(point))
    
    for i in range(resolution):
        for j in range(resolution):
            point = np.array([X[i, j], Y[i, j]])
            jacobian_matrix = numerical_jacobian(wrapper, point)
            det_jacobain[i, j] = np.linalg.det(jacobian_matrix)
            
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, det_jacobain, cmap='viridis')
    ax.set_title('Determinant of the Jacobian')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('det(J)')
    plt.show()
    
# Example usage

# Symbolic example
x, y = sp.symbols('x y')
funcs = [x**2 + y**2, sp.sin(x) * sp.cos(y)]
vars = [x, y]
jacobian_sym = symbolic_jacobian(funcs, vars)
print("Symbolic Jacobian:")
sp.pprint(jacobian_sym)

# Numerical example
def example_func(point):
    x, y = point
    return np.array([x**2 + y**2, np.sin(x) * np.cos(y)])

point = np.array([1.0, 2.0])
jacobian_num = numerical_jacobian(example_func, point)
print("\nNumerical Jacobian at point {}:".format(point))
print(jacobian_num)

# plot
plot_jacobian(example_func, x_range=(-2, 2), y_range=(-2, 2)) 