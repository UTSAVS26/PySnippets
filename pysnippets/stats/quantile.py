# quantile.py

import logging
from typing import List
import math

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def quantile(data: List[float], q: float) -> float:
    """
    Calculate the q-th quantile of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        q (float): The quantile to calculate (between 0 and 1).

    Returns:
        float: The q-th quantile of the numbers.

    Example:
        >>> quantile([1, 2, 3, 4, 5], 0.5)
        3
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not 0 <= q <= 1:
        logging.error(f"Invalid quantile value: {q}. Must be between 0 and 1.")
        raise ValueError("Quantile must be between 0 and 1")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    sorted_data = sorted(data)
    index = int(math.floor(q * (len(sorted_data) - 1)))
    quantile_value = sorted_data[index]
    logging.debug(f"Calculated quantile (q={q}): {quantile_value}")
    return quantile_value
