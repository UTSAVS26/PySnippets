import logging
from typing import List
from variance import variance

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def standard_deviation(data: List[float], population: bool = True) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[float]): A list of numbers.
        population (bool): If True, calculate population standard deviation; otherwise, sample standard deviation.

    Returns:
        float: The standard deviation of the numbers.

    Example:
        >>> standard_deviation([1, 2, 3, 4], population=True)
        1.118033988749895
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    std_dev = variance(data, population) ** 0.5
    
    # Log the calculation and the type of standard deviation being computed
    std_dev_type = "Population" if population else "Sample"
    logging.debug(f"Calculated {std_dev_type} standard deviation: {std_dev}")
    
    return std_dev