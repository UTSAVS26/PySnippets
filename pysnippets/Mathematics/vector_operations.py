import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def vector_addition(vec1: List[int], vec2: List[int]) -> List[int]:
    """Add two vectors element-wise.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        List[int]: The resultant vector after addition.
    """
    if len(vec1) != len(vec2):
        logging.error("Vectors must be of the same length.")
        raise ValueError("Vectors must be of the same length.")
    
    result = [a + b for a, b in zip(vec1, vec2)]
    logging.debug(f"Vector addition result: {result}")
    return result

# Additional vector operations with similar refactoring...

# Example usage
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Vector Addition:", vector_addition(v1, v2)) 
