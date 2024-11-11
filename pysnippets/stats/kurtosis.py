import logging
import numpy as np
from typing import List

# Configure logging
def configure_logging(level=logging.DEBUG):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def kurtosis(data: List[float], log_level=logging.DEBUG) -> float:
    """
    Calculate the kurtosis of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        log_level (int): The logging level to set (default is DEBUG).

    Returns:
        float: The kurtosis of the numbers.

    Example:
        >>> kurtosis([1, 2, 2, 3, 4])
        -1.5
    """
    # Configure logging level
    configure_logging(log_level)

    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")

    if len(data) < 4:
        logging.warning("Data has fewer than 4 elements, kurtosis calculation may not be meaningful.")
        return None  # Kurtosis is typically not calculated for small datasets

    # Remove NaN or infinite values from data
    data = [x for x in data if not np.isnan(x) and not np.isinf(x)]
    if len(data) < 4:
        logging.warning("After cleaning, data has fewer than 4 valid elements.")
        return None

    mean_value = np.mean(data)
    std_dev = np.std(data)
    
    if std_dev == 0:
        logging.warning("Standard deviation is zero, kurtosis is undefined.")
        return None  # Handle division by zero
    
    kurtosis_value = np.mean((data - mean_value) ** 4) / (std_dev ** 4) - 3
    logging.debug(f"Calculated kurtosis: {kurtosis_value}")
    return kurtosis_value