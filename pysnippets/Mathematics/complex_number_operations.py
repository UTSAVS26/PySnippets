# complex_number_operations.py

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
    real = c1[0] + c2[0]
    imag = c1[1] + c2[1]
    return (real, imag)

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
    real = c1[0] - c2[0]
    imag = c1[1] - c2[1]
    return (real, imag)

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
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imag = c1[0] * c2[1] + c1[1] * c2[0]
    return (real, imag)

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
