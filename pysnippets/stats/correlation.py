import logging
import numpy as np
from typing import List, Optional

# Configure logging
def configure_logging(level=logging.DEBUG):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def correlation(x: List[float], y: List[float], log_level=logging.DEBUG) -> Optional[float]:
    """
    Calculate the Pearson correlation coefficient between two lists of numbers.

    Args:
        x (List[float]): A list of numbers.
        y (List[float]): A list of numbers.
        log_level (int): The logging level to set (default is DEBUG).

    Returns:
        Optional[float]: The Pearson correlation coefficient, or None if not calculable.

    Example:
        >>> correlation([1, 2, 3], [2, 4, 6])
        1.0
    """
    # Configure logging level
    configure_logging(log_level)
    
    if not x or not y:
        logging.error("One or both input lists are empty.")
        raise ValueError("Lists cannot be empty")
    
    if len(x) != len(y):
        logging.error("Input lists have different lengths.")
        raise ValueError("Lists must have the same length")
    
    if len(x) == 1:  # Handle the case of a single value in each list
        logging.warning("Lists contain only one value each. Correlation is undefined.")
        return None
    
    # Remove NaN or infinite values from data if present
    x = [i for i in x if not np.isnan(i) and not np.isinf(i)]
    y = [i for i in y if not np.isnan(i) and not np.isinf(i)]
    
    if len(x) == 0 or len(y) == 0:
        logging.error("After cleaning, one or both lists are empty.")
        return None
    
    if not all(isinstance(n, (int, float)) for n in x + y):
        logging.error("Non-numeric value found in input lists.")
        raise ValueError("All elements in both lists must be numeric")
    
    # Calculate the correlation coefficient
    corr_coeff = np.corrcoef(x, y)[0, 1]
    logging.debug(f"Calculated correlation coefficient: {corr_coeff}")
    
    return corr_coeff