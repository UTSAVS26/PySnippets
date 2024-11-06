import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def vector_addition(v1: List[float], v2: List[float]) -> List[float]:
    """
    Add two vectors v1 and v2.

    Args:
        v1 (list of float): First vector.
        v2 (list of float): Second vector.

    Returns:
        list of float: The resulting vector after addition.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    result = [v1[i] + v2[i] for i in range(len(v1))]
    logging.debug(f"Added vectors {v1} and {v2} to get {result}")
    return result

# Example usage
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Vector Addition:", vector_addition(v1, v2)) 