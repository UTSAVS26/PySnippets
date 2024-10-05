# statistics.py

def mean(data):
    """
    Calculate the mean of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The mean of the numbers.

    Example:
        >>> mean([1, 2, 3, 4])
        2.5
    """
    if not data:
        raise ValueError("List is empty")
    return sum(data) / len(data)

def median(data):
    """
    Calculate the median of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The median of the numbers.

    Example:
        >>> median([1, 2, 3, 4, 5])
        3
    """
    if not data:
        raise ValueError("List is empty")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return (sorted_data[mid] + sorted_data[-mid - 1]) / 2 if n % 2 == 0 else sorted_data[mid]

def mode(data):
    """
    Calculate the mode of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        int or float: The mode of the numbers.

    Example:
        >>> mode([1, 2, 2, 3, 4])
        2
    """
    if not data:
        raise ValueError("List is empty")
    from collections import Counter
    count = Counter(data)
    return count.most_common(1)[0][0]
