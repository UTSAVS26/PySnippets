# quantile.py

def quantile(data, q):
    """
    Calculate the q-th quantile of a list of numbers.

    Args:
        data (list): A list of numbers.
        q (float): The quantile to calculate (between 0 and 1).

    Returns:
        float: The q-th quantile of the numbers.

    Example:
        >>> quantile([1, 2, 3, 4, 5], 0.5)
        3
    """
    if not data:
        raise ValueError("List is empty")
    
    if not (0 <= q <= 1):
        raise ValueError("Quantile must be between 0 and 1")
    
    # Ensure all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the data list must be numeric")
    
    sorted_data = sorted(data)
    index = int(q * (len(sorted_data) - 1))
    return sorted_data[index]
