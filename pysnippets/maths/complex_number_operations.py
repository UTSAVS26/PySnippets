import math
from typing import Tuple, Union


def _validate_complex(c: Tuple[Union[int, float], Union[int, float]]) -> None:
    """Helper function to validate complex number input."""
    if (
        not isinstance(c, tuple)
        or len(c) != 2
        or not all(isinstance(i, (int, float)) for i in c)
    ):
        raise TypeError("Input must be a tuple of two numbers (real, imag).")


def add_complex(
    c1: Tuple[Union[int, float], Union[int, float]],
    c2: Tuple[Union[int, float], Union[int, float]],
) -> Tuple[Union[int, float], Union[int, float]]:
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
    _validate_complex(c1)
    _validate_complex(c2)
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real, imag)


def subtract_complex(
    c1: Tuple[Union[int, float], Union[int, float]],
    c2: Tuple[Union[int, float], Union[int, float]],
) -> Tuple[Union[int, float], Union[int, float]]:
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
    _validate_complex(c1)
    _validate_complex(c2)
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real, imag)


def multiply_complex(
    c1: Tuple[Union[int, float], Union[int, float]],
    c2: Tuple[Union[int, float], Union[int, float]],
) -> Tuple[Union[int, float], Union[int, float]]:
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
    _validate_complex(c1)
    _validate_complex(c2)
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imag)


def divide_complex(
    c1: Tuple[Union[int, float], Union[int, float]],
    c2: Tuple[Union[int, float], Union[int, float]],
) -> Tuple[float, float]:
    """
    Division of two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The Division of the two complex numbers as (real, imag).

    Example:
        >>> divide_complex((3, 4), (1, 2))
        (-2.2, -0.4)
    """
    _validate_complex(c1)
    _validate_complex(c2)
    if c2 == (0, 0):
        raise ZeroDivisionError("Division by zero is not allowed")
    denominator = c2[0] ** 2 + c2[1] ** 2
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / denominator
    imag = (c1[1] * c2[0] - c1[0] * c2[1]) / denominator
    return (real, imag)


def conjugate_complex(
    c: Tuple[Union[int, float], Union[int, float]]
) -> Tuple[Union[int, float], Union[int, float]]:
    """
    Conjugate of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        tuple: The Conjugate of the complex number as (real, imag).

    Example:
        >>> conjugate_complex((3, 4))
        (3, -4)
    """
    _validate_complex(c)
    return (c[0], -c[1])


def modulus_complex(c: Tuple[Union[int, float], Union[int, float]]) -> float:
    """
    Modulus of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The Modulus of the complex number.

    Example:
        >>> modulus_complex((3, 4))
        5.0
    """
    _validate_complex(c)
    return math.sqrt(c[0] ** 2 + c[1] ** 2)


def argument_complex(c: Tuple[Union[int, float], Union[int, float]]) -> float:
    """
    Argument of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The Argument of the complex number in Radians.

    Example:
        >>> argument_complex((3, 4))
        0.9272952180016122
    """
    _validate_complex(c)
    return math.atan2(c[1], c[0])


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
