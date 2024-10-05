from variance import variance

def standard_deviation(data, population=True):
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (list): A list of numbers.
        population (bool): If True, calculate population standard deviation; otherwise, sample.

    Returns:
        float: The standard deviation of the numbers.

    Example:
        >>> standard_deviation([1, 2, 3, 4], population=True)
        1.118033988749895
    """
    return variance(data, population) ** 0.5
