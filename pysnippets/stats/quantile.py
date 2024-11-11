import logging
from typing import List
import math

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def quantile(data: List[float], q: float, interpolate: bool = False) -> float:
    """
    Calculate the q-th quantile of a list of numbers. Optionally, interpolate the result if the index isn't an integer.

    Args:
        data (List[float]): A list of numbers.
        q (float): The quantile to calculate (between 0 and 1).
        interpolate (bool): Whether to interpolate between values if necessary (default is False).

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
    n = len(sorted_data)
    index = q * (n - 1)
    
    if interpolate:
        # Linear interpolation if the index is not an integer
        lower = int(math.floor(index))
        upper = int(math.ceil(index))
        if lower == upper:
            quantile_value = sorted_data[lower]
        else:
            quantile_value = sorted_data[lower] + (index - lower) * (sorted_data[upper] - sorted_data[lower])
    else:
        # Regular method, just use the integer index
        quantile_value = sorted_data[int(math.floor(index))]
    
    logging.debug(f"Calculated quantile (q={q}): {quantile_value}")
    return quantile_value

def calculate_multiple_quantiles(data: List[float], quantiles: List[float], interpolate: bool = False) -> List[float]:
    """
    Calculate multiple quantiles at once.

    Args:
        data (List[float]): A list of numbers.
        quantiles (List[float]): A list of quantiles (values between 0 and 1).
        interpolate (bool): Whether to interpolate between values if necessary (default is False).

    Returns:
        List[float]: A list of quantiles.
    """
    return [quantile(data, q, interpolate) for q in quantiles]