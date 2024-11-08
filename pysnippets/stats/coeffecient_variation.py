# cv.py

import logging
import numpy as np
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def coefficient_of_variation(data: List[float]) -> float:
    """
    Calculate the Coefficient of Variation (CV) of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The CV, expressed as a percentage.

    Example:
        >>> coefficient_of_variation([10, 20, 30])
        57.735026918962575
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    mean_value = np.mean(data)
    std_dev = np.std(data)
    cv = (std_dev / mean_value) * 100
    logging.debug(f"Calculated CV: {cv}")
    return cv
