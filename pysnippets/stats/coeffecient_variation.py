import logging
import numpy as np
from typing import List, Optional

# Configure logging
def configure_logging(level=logging.DEBUG):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def coefficient_of_variation(data: List[float], log_level=logging.DEBUG) -> Optional[float]:
    """
    Calculate the Coefficient of Variation (CV) of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        log_level (int): The logging level to set (default is DEBUG).

    Returns:
        Optional[float]: The CV, expressed as a percentage, or None if CV can't be calculated.

    Example:
        >>> coefficient_of_variation([10, 20, 30])
        57.735026918962575
    """
    # Configure logging level
    configure_logging(log_level)
    
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    if len(data) == 1:
        logging.warning("Data contains only one value. CV is undefined.")
        return None  # CV is undefined for a single data point

    # Remove NaN values from data if present
    data = [x for x in data if not np.isnan(x)]
    
    mean_value = np.mean(data)
    
    # Avoid division by zero
    if mean_value == 0:
        logging.warning("Mean of data is zero. CV is undefined.")
        return None
    
    std_dev = np.std(data)
    
    # Handle the case where standard deviation is zero
    if std_dev == 0:
        logging.warning("Standard deviation is zero. CV is undefined.")
        return None

    cv = (std_dev / mean_value) * 100
    logging.debug(f"Calculated CV: {cv}%")
    
    return cv