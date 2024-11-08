# correlation.py

import logging
import numpy as np
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def correlation(x: List[float], y: List[float]) -> float:
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.

    Args:
        x (List[float]): A list of numbers.
        y (List[float]): A list of numbers.

    Returns:
        float: The Pearson correlation coefficient.

    Example:
        >>> correlation([1, 2, 3], [2, 4, 6])
        1.0
    """
    if not x or not y:
        logging.error("One or both input lists are empty.")
        raise ValueError("Lists cannot be empty")
    
    if len(x) != len(y):
        logging.error("Input lists have different lengths.")
        raise ValueError("Lists must have the same length")
    
    if not all(isinstance(n, (int, float)) for n in x + y):
        logging.error("Non-numeric value found in input lists.")
        raise ValueError("All elements in both lists must be numeric")
    
    corr_coeff = np.corrcoef(x, y)[0, 1]
    logging.debug(f"Calculated correlation coefficient: {corr_coeff}")
    return corr_coeff
