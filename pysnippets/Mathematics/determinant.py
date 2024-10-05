# determinant_calculation.py

def determinant(matrix):
    """
    Compute the determinant of a square matrix.

    Args:
        matrix (list of list of int/float): The square matrix for which the determinant is to be calculated.

    Returns:
        int/float: The determinant of the matrix.

    Raises:
        ValueError: If the matrix is not square (number of rows must equal number of columns).

    Example:
        >>> matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        >>> determinant(matrix)
        -34
    """
    # Check if the matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square (same number of rows and columns).")

    # Base case for 2x2 matrix
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case for larger matrices
    det = 0
    for c in range(n):
        # Calculate the minor matrix
        minor = [row[:c] + row[c+1:] for row in matrix[1:]]
        # Recursive call to determinant for the minor
        det += ((-1) ** c) * matrix[0][c] * determinant(minor)

    return det

# Example usage
if __name__ == "__main__":
    # Example usage of the function
    matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    result = determinant(matrix)
    print(result)
