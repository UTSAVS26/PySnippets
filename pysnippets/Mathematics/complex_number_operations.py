import logging
from typing import Tuple

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def add_complex(c1: Tuple[float, float], c2: Tuple[float, float]) -> Tuple[float, float]:
    """
    Add two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The sum of the two complex numbers as (real, imag).
    """
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    logging.debug(f"Adding {c1} and {c2} to get {(real, imag)}")
    return (real, imag)

def subtract_complex(c1: Tuple[float, float], c2: Tuple[float, float]) -> Tuple[float, float]:
    """
    Subtract the second complex number from the first.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The difference of the two complex numbers as (real, imag).
    """
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    logging.debug(f"Subtracting {c2} from {c1} to get {(real, imag)}")
    return (real, imag)

def multiply_complex(c1: Tuple[float, float], c2: Tuple[float, float]) -> Tuple[float, float]:
    """
    Multiply two complex numbers.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The product of the two complex numbers as (real, imag).
    """
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c2[1] + c1[1] * c2[0]
    logging.debug(f"Multiplying {c1} and {c2} to get {(real, imag)}")
    return (real, imag)

# Example usage
if __name__ == "__main__":
    c1 = (1, 2)
    c2 = (3, 4)

    sum_result = add_complex(c1, c2)
    print("Sum:", sum_result)

    difference_result = subtract_complex(c1, c2)
    print("Difference:", difference_result)

    product_result = multiply_complex(c1, c2)
    print("Product:", product_result) 