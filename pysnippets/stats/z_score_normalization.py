# statistics.py (continued)

import logging
from typing import List
from mean_median_mode import mean
from standard_deviation import standard_deviation

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def z_score_normalization(data: List[float]) -> List[float]:
    """
    Normalize a list of numbers using Z-score normalization.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        List[float]: The normalized values.

    Example:
        >>> z_score_normalization([1, 2, 3, 4, 5])
        [-1.4142135623730951, -0.7071067811865475, 0.0, 0.7071067811865475, 1.4142135623730951]
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    mean_value = mean(data)
    std_dev = standard_deviation(data)
    normalized_data = [(x - mean_value) / std_dev for x in data]
    logging.debug(f"Calculated Z-score normalized data: {normalized_data}")
    return normalized_data
