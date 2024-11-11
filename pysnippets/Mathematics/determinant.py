import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def determinant(matrix: List[List[float]]) -> float:
    """
    Compute the determinant of a square matrix.

    Args:
        matrix (list of list of float): The square matrix for which the determinant is to be calculated.

    Returns:
        float: The determinant of the matrix.

    Raises:
        ValueError: If the matrix is not square (number of rows must equal number of columns).
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square (same number of rows and columns).")

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(n):
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)

    logging.debug(f"Determinant of matrix {matrix} is {det}")
    return det

# Example usage
if __name__ == "__main__":
    matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    result = determinant(matrix)
    print("Determinant:", result) 