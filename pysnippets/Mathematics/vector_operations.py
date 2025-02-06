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

def vector_substraction(vec1: List[int], vec2: List[int]) -> List[int]:
    """Substract two vectors element-wise.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        List[int]: The resultant vector after substraction.
    """
    if len(vec1) != len(vec2):
        logging.error("Vectors must be of the same length.")
        raise ValueError("Vectors must be of the same length.")
    
    result = [a - b for a, b in zip(vec1, vec2)]
    logging.debug(f"Vector substraction result: {result}")
    return result


def vector_division(vec1: List[int], vec2: List[int]) -> List[int]:
    """Divide two vectors element-wise.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        List[int]: The resultant vector after division.
    """
    if len(vec1) != len(vec2):
        logging.error("Vectors must be of the same length.")
        raise ValueError("Vectors must be of the same length.")
    
    result = [a / b for a, b in zip(vec1, vec2)]
    logging.debug(f"Vector division result: {result}")
    return result

def dot_product(vec1: List[int], vec2: List[int]) -> int:
    """Calculate the dot product of two vectors.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        int: The dot product of the two vectors.
    """
    if len(vec1) != len(vec2):
        logging.error("Vectors must be of the same length.")
        raise ValueError("Vectors must be of the same length.")
    
    result = sum([a * b for a, b in zip(vec1, vec2)])
    logging.debug(f"Dot product result: {result}")
    return result

def cross_product(vec1: List[int], vec2: List[int]) -> List[int]:
    """Calculate the cross product of two vectors.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        List[int]: The cross product of the two vectors.
    """
    if len(vec1) != len(vec2):
        logging.error("Vectors must be of the same length.")
        raise ValueError("Vectors must be of the same length.")
    
    if len(vec1) != 3:
        logging.error("Cross product is only defined for 3D vectors.")
        raise ValueError("Cross product is only defined for 3D vectors.")
    
    result = [
        vec1[1] * vec2[2] - vec1[2] * vec2[1],
        vec1[2] * vec2[0] - vec1[0] * vec2[2],
        vec1[0] * vec2[1] - vec1[1] * vec2[0]
    ]
    logging.debug(f"Cross product result: {result}")
    return result

def magnitude(vec: List[int]) -> float:
    """Calculate the magnitude of a vector.
    Args:
        vec (List[int]): The vector.
    Returns:
        float: The magnitude of the vector.
    """
    result = sum([a ** 2 for a in vec]) ** 0.5
    logging.debug(f"Magnitude result: {result}")
    return result

def normalization(vec: List[int]) -> List[int]:
    """Normalize a vector.
    Args:
        vec (List[int]): The vector.
    Returns:
        List[int]: The normalized vector.
    """
    mag = magnitude(vec)
    result = [a / mag for a in vec]
    logging.debug(f"Normalization result: {result}")
    return result

def vector_angle(vec1: List[int], vec2: List[int]) -> float:
    """Calculate the angle between two vectors.
    Args:
        vec1 (List[int]): The first vector.
        vec2 (List[int]): The second vector.
    Returns:
        float: The angle between the two vectors.
    """
    dot = dot_product(vec1, vec2)
    mag1 = magnitude(vec1)
    mag2 = magnitude(vec2)
    result = dot / (mag1 * mag2)
    logging.debug(f"Vector angle result: {result}")
    return result

def tensor_vector_product(tensor: List[List[int]], vec: List[int]) -> List[int]:
    """Calculate the product of a tensor and a vector.
    Args:
        tensor (List[List[int]]): The tensor.
        vec (List[int]): The vector.
    Returns:
        List[int]: The resultant vector after the product.
    """
    if len(tensor) != len(vec):
        logging.error("Tensor and vector must be of the same length.")
        raise ValueError("Tensor and vector must be of the same length.")
    
    result = [sum([a * b for a, b in zip(row, vec)]) for row in tensor]
    logging.debug(f"Tensor vector product result: {result}")
    return result


# Example usage
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Vector Addition:", vector_addition(v1, v2)) 
    
    print("Vector Substraction:", vector_substraction(v1, v2))
    print("Vector Division:", vector_division(v1, v2))
    print("Dot Product:", dot_product(v1, v2))
    print("Cross Product:", cross_product(v1, v2))
    print("Magnitude:", magnitude(v1))
    print("Normalization:", normalization(v1))
    print("Vector Angle:", vector_angle(v1, v2))
    print("Tensor Vector Product:", tensor_vector_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], v1))
    
    
