# iqr.py

import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def iqr(data: List[float]) -> Tuple[float, float, float]:
    """
    Calculate the Interquartile Range (IQR) of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        Tuple[float, float, float]: The first quartile (Q1), third quartile (Q3), and the IQR.

    Example:
        >>> iqr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        (3.25, 7.75, 4.5)
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    Q1_index = int(0.25 * (n - 1))
    Q3_index = int(0.75 * (n - 1))
    
    Q1 = sorted_data[Q1_index]
    Q3 = sorted_data[Q3_index]
    iqr_value = Q3 - Q1
    logging.debug(f"Calculated IQR: Q1={Q1}, Q3={Q3}, IQR={iqr_value}")
    return Q1, Q3, iqr_value
