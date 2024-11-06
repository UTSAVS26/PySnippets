import logging
from typing import List

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

# Example usage
if __name__ == "__main__":
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[7, 8], [9, 10], [11, 12]]
    result = matrix_multiplication(A, B)
    print(result) 