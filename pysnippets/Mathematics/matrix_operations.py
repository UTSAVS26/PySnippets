import logging
from typing import List
import numpy as np

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def matrix_addition(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices A and B.

    Args:
        A (list of list of float): First matrix.
        B (list of list of float): Second matrix.

    Returns:
        list of list of float: The resulting matrix after addition.

    Raises:
        ValueError: If the dimensions of the two matrices are not the same.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("The dimensions of the two matrices must be the same.")

    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    logging.debug(f"Added matrices {A} and {B} to get {result}")
    return result

def matrix_multiplication(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices A and B.

    Args:
        A (list of list of float): First matrix.
        B (list of list of float): Second matrix.

    Returns:
        list of list of float: The resulting matrix after multiplication.

    Raises:
        ValueError: If the number of columns in A does not match the number of rows in B.
    """
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must match number of rows in B.")

    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    logging.debug(f"Multiplied matrices {A} and {B} to get {result}")
    return result


def matrix_transpose(A):
    """
    Transpose a matrix A.

    Args:
        A (list of list of float): The matrix to be transposed.

    Returns:
        list of list of float: The transposed matrix.
    """
    result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
    logging.debug(f"Transposed matrix {A} to get {result}")
    return result

def matrix_scalar_multiplication(A, scalar):
    """
    Multiply a matrix A by a scalar.

    Args:
        A (list of list of float): The matrix to be multiplied.
        scalar (float): The scalar to multiply the matrix by.

    Returns:
        list of list of float: The resulting matrix after scalar multiplication.
    """
    result = [[A[i][j] * scalar for j in range(len(A[0]))] for i in range(len(A))]
    logging.debug(f"Multiplied matrix {A} by scalar {scalar} to get {result}")
    return result

def determinant(A):
    """
    Compute the determinant of a square matrix A.

    Args:
        A (list of list of float): The matrix to compute the determinant of.

    Returns:
        float: The determinant of the matrix.
    """
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to compute determinant.")

    if len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    else:
        det = 0
        for i in range(len(A)):
            minor = [row[:i] + row[i+1:] for row in A[1:]]
            det += ((-1) ** i) * A[0][i] * determinant(minor)
        return det
    
def matrix_inverse(A):
    """
    Compute the inverse of a square matrix A.

    Args:
        A (list of list of float): The matrix to compute the inverse of.

    Returns:
        list of list of float: The inverse of the matrix.

    Raises:
        ValueError: If the matrix is not square or is singular (i.e., its determinant is zero).
    """
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to compute inverse.")

    det = determinant(A)
    if det == 0:
        raise ValueError("Matrix is singular and does not have an inverse.")

    adjugate = [[((-1) ** (i + j)) * determinant([row[:j] + row[j+1:] for row in A[:i] + A[i+1:]]) for j in range(len(A))] for i in range(len(A))]
    inverse = matrix_scalar_multiplication(matrix_transpose(adjugate), 1 / det)
    
    return inverse

def matrix_trace(A):
    """
    Compute the trace of a square matrix A.

    Args:
        A (list of list of float): The matrix to compute the trace of.

    Returns:
        float: The trace of the matrix.
    """
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to compute trace.")

    return sum(A[i][i] for i in range(len(A)))

def eigenvalues_and_eigenvectors(A):
    """
    Compute the eigenvalues and eigenvectors of a square matrix A.

    Args:
        A (list of list of float): The matrix to compute the eigenvalues and eigenvectors of.

    Returns:
        tuple: A tuple containing:
            - list of float: The eigenvalues of the matrix.
            - list of list of float: The eigenvectors of the matrix.
    """
    if len(A) != len(A[0]):
        raise ValueError("Matrix must be square to compute eigenvalues and eigenvectors.")

    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]

    print("Matrix Addition:")
    print(matrix_addition(A, B))

    print("\nMatrix Multiplication:")
    print(matrix_multiplication(A, B))

    print("\nMatrix Transpose:")
    print(matrix_transpose(A))

    print("\nMatrix Scalar Multiplication:")
    print(matrix_scalar_multiplication(A, 2))

    print("\nDeterminant:")
    print(determinant(A))

    print("\nMatrix Inverse:")
    print(matrix_inverse(A))

    print("\nMatrix Trace:")
    print(matrix_trace(A))

    print("\nEigenvalues and Eigenvectors:")
    eigenvalues, eigenvectors = eigenvalues_and_eigenvectors(A)
    print("Eigenvalues:", eigenvalues)
    print("Eigenvectors:", eigenvectors)
