# correlation.py

import numpy as np

def correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.

    Args:
        x (list): A list of numbers.
        y (list): A list of numbers.

    Returns:
        float: The Pearson correlation coefficient.

    Example:
        >>> correlation([1, 2, 3], [2, 4, 6])
        1.0
    """
    if not x or not y:
        raise ValueError("Lists cannot be empty")
    
    if len(x) != len(y):
        raise ValueError("Lists must have the same length")
    
    # Ensure all elements in the lists are numeric
    if not all(isinstance(n, (int, float)) for n in x + y):
        raise ValueError("All elements in both lists must be numeric")
    
    return np.corrcoef(x, y)[0, 1]
