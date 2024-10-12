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
    
def minor(matrix, i, j):
    """
    Compute the minor of a matrix by removing the i-th row and j-th column.

    Args:
        matrix (list of list of int/float): The original matrix.
        i (int): The row index to remove.
        j (int): The column index to remove.

    Returns:
        list of list of int/float: The minor matrix.

    Example:
        >>> matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        >>> minor(matrix, 0, 1)
        [[0, 4], [5, 0]]
    """
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def cofactor(matrix):
    """
    Compute the cofactor matrix of a square matrix.

    Args:
        matrix (list of list of int/float): The square matrix for which the cofactor matrix is to be calculated.

    Returns:
        list of list of int/float: The cofactor matrix.

    Example:
        >>> matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        >>> cofactor(matrix)
        [[-24, 20, -5], [12, -15, 4], [-2, 3, -1]]
    """
    n = len(matrix)
    cofactors = []
    for i in range(n):
        cofactor_row = []
        for j in range(n):
            minor_matrix = minor(matrix, i, j)
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor_matrix))
        cofactors.append(cofactor_row)
    return cofactors

def adjugate(matrix):
    """
    Compute the adjugate (transpose of the cofactor matrix) of a square matrix.

    Args:
        matrix (list of list of int/float): The square matrix for which the adjugate is to be calculated.

    Returns:
        list of list of int/float: The adjugate matrix.

    Example:
        >>> matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
        >>> adjugate(matrix)
        [[-24, 12, -2], [20, -15, 3], [-5, 4, -1]]
    """
    return list(map(list, zip(*cofactor(matrix))))


# Example usage
if __name__ == "__main__":
    # Example usage of the function
    matrix = [[1, 2, 3], [0, 1, 4], [5, 6, 0]]
    result = determinant(matrix)
    print(result)
