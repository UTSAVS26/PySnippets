# complex_number_operations.py
import math


def add_complex(c1, c2):
    """
    Add two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The sum of the two complex numbers as (real, imag).

    Example:
        >>> add_complex((1, 2), (3, 4))
        (4, 6)
    """
    try:
        real = c1[0] + c2[0]
        imag = c1[1] + c2[1]
        return (real, imag)
    except Exception as e:
        return f"Error in addition: {e}"


def subtract_complex(c1, c2):
    """
    Subtract the second complex number from the first.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The difference of the two complex numbers as (real, imag).

    Example:
        >>> subtract_complex((5, 7), (2, 3))
        (3, 4)
    """
    try:
        real = c1[0] - c2[0]
        imag = c1[1] - c2[1]
        return (real, imag)
    except Exception as e:
        return f"Error in subtration: {e}"


def multiply_complex(c1, c2):
    """
    Multiply two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The product of the two complex numbers as (real, imag).

    Example:
        >>> multiply_complex((1, 2), (3, 4))
        (-5, 10)
    """
    try:
        real = c1[0] * c2[0] - c1[1] * c2[1]
        imag = c1[0] * c2[1] + c1[1] * c2[0]
        return (real, imag)
    except Exception as e:
        return f"Error in multiplication: {e}"


def divide_complex(c1, c2):
    """
    Division of two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The Divison of the two complex numbers as (real, imag).

    Example:
        >>> divide_complex((3, 4), (1, 2))
        (-2.2, -0.4)
    """
    try:
        if c2 == (0, 0):
            raise ZeroDivisionError("Divison by zero is not allowed")
        denominator = c2[0] ** 2 + c2[1] ** 2
        real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominator
        imag = (c1[1] * c2[0] - c1[0] * c2[1]) / denominator
        return (real, imag)
    except Exception as e:
        return f"Error in division: {e}"


def conjugate_complex(c):
    """
    Conjugate of a complex numbers.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        tuple: The Conjugate of the complex numbers as (real, imag).

    Example:
        >>> conjugate_complex((3, 4))
        (3, -4)
    """
    try:
        return (c[0], -c[1])
    except Exception as e:
        return f"Error in conjugation: {e}"


def modulus_complex(c):
    """
    Modulus of a complex numbers.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The Modulus of the complex numbers.

    Example:
        >>> modulus_complex((3, 4))
        5.0
    """
    try:
        return math.sqrt(c[0] ** 2 + c[1] ** 2)
    except Exception as e:
        return f"Error in modulus calculation: {e}"


def argument_complex(c):
    """
    Argument of a complex numbers.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The Argument of the complex numbers in Radians.

    Example:
        >>> argument_complex((3, 4))
        0.9272952180016122
    """
    try:
        return math.atan2(c[1], c[0])
    except Exception as e:
        return f"Error in arguement calculation: {e}"


# Example usage
if __name__ == "__main__":
    # Example usage of the functions
    c1 = (1, 2)  # 1 + 2i
    c2 = (3, 4)  # 3 + 4i

    sum_result = add_complex(c1, c2)
    print("Sum:", sum_result)

    difference_result = subtract_complex(c1, c2)
    print("Difference:", difference_result)

    product_result = multiply_complex(c1, c2)
    print("Product:", product_result)

    division_result = divide_complex(c1, c2)
    print("Division:", division_result)

    conjugate_result = conjugate_complex(c1)
    print("Conjugate of c1:", conjugate_result)

    modulus_result = modulus_complex(c1)
    print("Modulus of c1:", modulus_result)

    argument_result = argument_complex(c1)
    print("Argument of c1:", argument_result)
