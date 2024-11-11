import logging
from typing import List, Tuple
import numpy as np

# Configure logging
def configure_logging(level=logging.DEBUG):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def iqr(data: List[float], log_level=logging.DEBUG) -> Tuple[float, float, float]:
    """
    Calculate the Interquartile Range (IQR) of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        log_level (int): The logging level to set (default is DEBUG).

    Returns:
        Tuple[float, float, float]: The first quartile (Q1), third quartile (Q3), and the IQR.

    Example:
        >>> iqr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        (3.25, 7.75, 4.5)
    """
    # Configure logging level
    configure_logging(log_level)

    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    # Remove NaN or infinite values
    data = [x for x in data if not np.isnan(x) and not np.isinf(x)]
    if len(data) < 4:
        logging.warning("Data has fewer than 4 elements, quartile calculation may not be meaningful.")
        return None  # IQR is typically not calculated with fewer than 4 data points
    
    sorted_data = sorted(data)
    Q1 = np.percentile(sorted_data, 25)
    Q3 = np.percentile(sorted_data, 75)
    iqr_value = Q3 - Q1
    
    logging.debug(f"Calculated IQR: Q1={Q1}, Q3={Q3}, IQR={iqr_value}")
    return Q1, Q3, iqr_value