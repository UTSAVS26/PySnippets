import logging
from typing import List, Union
from collections import Counter

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def mean(data: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The mean of the numbers.

    Example:
        >>> mean([1, 2, 3, 4])
        2.5
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    mean_value = sum(data) / len(data)
    logging.debug(f"Calculated mean: {mean_value}")
    return mean_value

def median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        float: The median of the numbers.

    Example:
        >>> median([1, 2, 3, 4, 5])
        3
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")

    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    median_value = (sorted_data[mid] + sorted_data[-mid - 1]) / 2 if n % 2 == 0 else sorted_data[mid]
    logging.debug(f"Calculated median: {median_value}")
    return median_value

def mode(data: List[float]) -> Union[int, float, List[Union[int, float]]]:
    """
    Calculate the mode of a list of numbers. Returns all modes if there are multiple.

    Args:
        data (List[float]): A list of numbers.

    Returns:
        Union[int, float, List[Union[int, float]]]: The mode of the numbers or a list of modes if multiple exist.

    Example:
        >>> mode([1, 2, 2, 3, 4])
        2
    """
    if not data:
        logging.error("Input data list is empty.")
        raise ValueError("List is empty")
    if not all(isinstance(x, (int, float)) for x in data):
        logging.error("Non-numeric value found in data list.")
        raise ValueError("All elements in the data list must be numeric")
    
    count = Counter(data)
    most_common = count.most_common()
    max_count = most_common[0][1]
    modes = [value for value, count in most_common if count == max_count]

    logging.debug(f"Calculated mode(s): {modes}")
    return modes[0] if len(modes) == 1 else modes