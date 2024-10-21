# kurtosis.py

import numpy as np

def kurtosis(data):
    """
    Calculate the kurtosis of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The kurtosis of the numbers.

    Example:
        >>> kurtosis([1, 2, 2, 3, 4])
        -1.5
    """
    if not data:
        raise ValueError("List is empty")
    
    # Ensure all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the data list must be numeric")
    
    return np.mean((data - np.mean(data))**4) / (np.std(data)**4) - 3
