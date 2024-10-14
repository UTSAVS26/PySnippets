# vector_operations.py

import math

def vector_addition(v1, v2):
    """
    Add two vectors v1 and v2.

    Args:
        v1 (list of int/float): First vector.
        v2 (list of int/float): Second vector.

    Returns:
        list of int/float: The resulting vector after addition.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.

    Example:
        >>> v1 = [1, 2, 3]
        >>> v2 = [4, 5, 6]
        >>> vector_addition(v1, v2)
        [5, 7, 9]
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtraction(v1, v2):
    """
    Subtract vector v2 from v1.

    Args:
        v1 (list of int/float): First vector.
        v2 (list of int/float): Second vector.

    Returns:
        list of int/float: The resulting vector after subtraction.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.

    Example:
        >>> v1 = [4, 5, 6]
        >>> v2 = [1, 2, 3]
        >>> vector_subtraction(v1, v2)
        [3, 3, 3]
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    return [v1[i] - v2[i] for i in range(len(v1))]

def scalar_multiplication(v, scalar):
    """
    Multiply a vector v by a scalar.

    Args:
        v (list of int/float): The vector.
        scalar (int/float): The scalar to multiply by.

    Returns:
        list of int/float: The resulting vector after scalar multiplication.

    Example:
        >>> v = [1, 2, 3]
        >>> scalar_multiplication(v, 3)
        [3, 6, 9]
    """
    return [element * scalar for element in v]

def dot_product(v1, v2):
    """
    Compute the dot product of two vectors v1 and v2.

    Args:
        v1 (list of int/float): First vector.
        v2 (list of int/float): Second vector.

    Returns:
        int/float: The dot product of the two vectors.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.

    Example:
        >>> v1 = [1, 2, 3]
        >>> v2 = [4, 5, 6]
        >>> dot_product(v1, v2)
        32
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    return sum(v1[i] * v2[i] for i in range(len(v1)))

def vector_magnitude(v):
    """
    Compute the magnitude (length) of a vector.

    Args:
        v (list of int/float): The vector.

    Returns:
        float: The magnitude of the vector.

    Example:
        >>> v = [3, 4]
        >>> vector_magnitude(v)
        5.0
    """
    return math.sqrt(sum(element ** 2 for element in v))

def vector_normalization(v):
    """
    Normalize a vector (i.e., scale it to have a magnitude of 1).

    Args:
        v (list of int/float): The vector.

    Returns:
        list of float: The normalized vector.

    Example:
        >>> v = [3, 4]
        >>> vector_normalization(v)
        [0.6, 0.8]
    """
    magnitude = vector_magnitude(v)
    if magnitude == 0:
        raise ValueError("Cannot normalize a zero vector.")
    
    return [element / magnitude for element in v]

def cross_product(v1, v2):
    """
    Compute the cross product of two 3D vectors.

    Args:
        v1 (list of int/float): First vector (3D).
        v2 (list of int/float): Second vector (3D).

    Returns:
        list of int/float: The resulting vector after cross product.

    Raises:
        ValueError: If the vectors are not 3D.

    Example:
        >>> v1 = [1, 0, 0]
        >>> v2 = [0, 1, 0]
        >>> cross_product(v1, v2)
        [0, 0, 1]
    """
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")

    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def angle_between_vectors(v1, v2):
    """
    Calculate the angle (in radians) between two vectors.

    Args:
        v1 (list of int/float): First vector.
        v2 (list of int/float): Second vector.

    Returns:
        float: The angle in radians between the two vectors.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.

    Example:
        >>> v1 = [1, 0]
        >>> v2 = [0, 1]
        >>> angle_between_vectors(v1, v2)
        1.5707963267948966  # (90 degrees in radians)
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    dot_prod = dot_product(v1, v2)
    mag_v1 = vector_magnitude(v1)
    mag_v2 = vector_magnitude(v2)

    return math.acos(dot_prod / (mag_v1 * mag_v2))

def projection(v1, v2):
    """
    Project vector v1 onto vector v2.

    Args:
        v1 (list of int/float): First vector.
        v2 (list of int/float): Second vector.

    Returns:
        list of float: The projection of v1 onto v2.

    Raises:
        ValueError: If the dimensions of the two vectors are not the same.

    Example:
        >>> v1 = [1, 2, 3]
        >>> v2 = [4, 5, 6]
        >>> projection(v1, v2)
        [0.6623376623376623, 0.827922077922078, 0.9935064935064936]
    """
    if len(v1) != len(v2):
        raise ValueError("The dimensions of the two vectors must be the same.")

    dot_prod = dot_product(v1, v2)
    mag_v2_squared = vector_magnitude(v2) ** 2

    scalar_proj = dot_prod / mag_v2_squared

    return scalar_multiplication(v2, scalar_proj)

# Example usage
if __name__ == "__main__":
    v1 = [1, 2, 3, 4]
    v2 = [4, 5, 6, 5]
    
    print("Vector Addition:", vector_addition(v1, v2))
    print("Vector Subtraction:", vector_subtraction(v1, v2))
    print("Dot Product:", dot_product(v1, v2))
    # print("Cross Product:", cross_product(v1, v2))
    print("Angle Between Vectors:", angle_between_vectors(v1, v2))
    print("Projection of v1 onto v2:", projection(v1, v2))
