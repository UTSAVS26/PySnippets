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
        population (bool): If True, calculate population standard deviation; otherwise, sample.

    Returns:
        float: The standard deviation of the numbers.

    Example:
        >>> standard_deviation([1, 2, 3, 4], population=True)
        1.118033988749895
    """
    std_dev = variance(data, population) ** 0.5
    logging.debug(f"Calculated standard deviation: {std_dev}")
    return std_dev
