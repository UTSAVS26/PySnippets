# statistics.py (continued)

from mean_median_mode import mean

def variance(data, population=True):
    """
    Calculate the variance of a list of numbers.

    Args:
        data (list): A list of numbers.
        population (bool): If True, calculate population variance; otherwise, sample variance.

    Returns:
        float: The variance of the numbers.

    Example:
        >>> variance([1, 2, 3, 4], population=True)
        1.25
    """
    if not data:
        raise ValueError("List is empty")
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / (len(data) if population else len(data) - 1)
