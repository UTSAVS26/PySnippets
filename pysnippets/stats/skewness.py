# skewness.py

import numpy as np

def skewness(data):
    """
    Calculate the skewness of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The skewness of the numbers.

    Example:
        >>> skewness([1, 2, 2, 3, 4])
        0.0
    """
    if not data:
        raise ValueError("List is empty")
    
    # Ensure all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the data list must be numeric")
    
    return np.mean((data - np.mean(data))**3) / (np.std(data)**3)
