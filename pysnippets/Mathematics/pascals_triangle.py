import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def pascals_triangle(rows: int) -> List[List[int]]:
    """
    Generate Pascal's Triangle up to a given number of rows.

    Args:
        rows (int): The number of rows to generate in Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle as a list of rows, where each row is a list of integers.
    """
    if rows <= 0:
        raise ValueError("'rows' must be a positive integer.")
    
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    logging.debug(f"Generated Pascal's Triangle with {rows} rows: {triangle}")
    return triangle

# Example usage
if __name__ == "__main__":
    print(pascals_triangle(5)) 