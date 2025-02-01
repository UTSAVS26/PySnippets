import logging
import math
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

def division(c1: Tuple[float, float], c2: Tuple[float, float]) -> Tuple[float, float]:
    """
    Divide the first complex number by the second.

    Args:
        c1 (tuple): The first complex number as (real, imag).
        c2 (tuple): The second complex number as (real, imag).

    Returns:
        tuple: The division of the two complex numbers as (real, imag).
    """
    real = (c1[0] * c2[0] + c1[1] * c2[1]) / (c2[0] ** 2 + c2[1] ** 2)
    imag = (c1[1] * c2[0] - c1[0] * c2[1]) / (c2[0] ** 2 + c2[1] ** 2)
    logging.debug(f"Dividing {c1} by {c2} to get {(real, imag)}")
    return (real, imag)

def magnitude(c: Tuple[float, float]) -> float:
    """
    Calculate the magnitude of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The magnitude of the complex number.
    """
    mag = (c[0] ** 2 + c[1] ** 2) ** 0.5
    logging.debug(f"Calculating the magnitude of {c} as {mag}")
    return mag  

def conjugate(c: Tuple[float, float]) -> Tuple[float, float]:
    """
    Calculate the conjugate of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        tuple: The conjugate of the complex number as (real, imag).
    """
    logging.debug(f"Calculating the conjugate of {c}")
    return (c[0], -c[1])

def argument(c: Tuple[float, float]) -> float:
    """
    Calculate the argument of a complex number.

    Args:
        c (tuple): The complex number as (real, imag).

    Returns:
        float: The argument of the complex number.
    """
    arg = math.atan2(c[1], c[0])
    logging.debug(f"Calculating the argument of {c} as {arg}")
    return arg

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
    
    division_result = division(c1, c2)
    print("Division:", division_result)
    
    mag = magnitude(c1)
    print("Magnitude:", mag)
    
    conj = conjugate(c1)
    print("Conjugate:", conj)
    
    arg = argument(c1)
    print("Argument:", arg)
    
