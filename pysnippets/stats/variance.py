import logging
from typing import List
from mean_median_mode import mean

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def variance(data: List[float], population: bool = True) -> float:
    """
    Calculate the variance of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        population (bool): If True, calculate population variance; otherwise, sample variance.

    Returns:
        float: The variance of the numbers.

    Example:
        >>> variance([1, 2, 3, 4], population=True)
        1.25
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    mean_value = mean(data)
    denominator = len(data) if population else len(data) - 1
    variance_value = sum((x - mean_value) ** 2 for x in data) / denominator
    
    # Log the variance type and value
    variance_type = "Population" if population else "Sample"
    logging.debug(f"Calculated {variance_type} variance: {variance_value}")
    
    return variance_value