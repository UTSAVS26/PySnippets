# statistics.py (continued)

from mean_median_mode import mean
from standard_deviation import standard_deviation

def z_score_normalization(data):
    """
    Normalize a list of numbers using Z-score normalization.

    Args:
        data (list): A list of numbers.

    Returns:
        list: The normalized values.

    Example:
        >>> z_score_normalization([1, 2, 3, 4, 5])
        [-1.4142135623730951, -0.7071067811865475, 0.0, 0.7071067811865475, 1.4142135623730951]
    """
    if not data:
        raise ValueError("List is empty")
    mean_value = mean(data)
    std_dev = standard_deviation(data)
    return [(x - mean_value) / std_dev for x in data]
