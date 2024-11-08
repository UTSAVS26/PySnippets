# kurtosis.py

import logging
import numpy as np
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def kurtosis(data: List[float]) -> float:
    """
    Calculate the kurtosis of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The kurtosis of the numbers.

    Example:
        >>> kurtosis([1, 2, 2, 3, 4])
        -1.5
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    mean_value = np.mean(data)
    std_dev = np.std(data)
    kurtosis_value = np.mean((data - mean_value) ** 4) / (std_dev ** 4) - 3
    logging.debug(f"Calculated kurtosis: {kurtosis_value}")
    return kurtosis_value
