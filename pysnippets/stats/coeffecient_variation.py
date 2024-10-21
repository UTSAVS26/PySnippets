# cv.py

import numpy as np

def coefficient_of_variation(data):
    """
    Calculate the Coefficient of Variation (CV) of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The CV, expressed as a percentage.

    Example:
        >>> coefficient_of_variation([10, 20, 30])
        0.5773502691896257
    """
    if not data:
        raise ValueError("List is empty")
    
    # Ensure all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the data list must be numeric")
    
    mean = np.mean(data)
    std_dev = np.std(data)
    return (std_dev / mean) * 100
