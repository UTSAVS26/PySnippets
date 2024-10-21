# iqr.py

def iqr(data):
    """
    Calculate the Interquartile Range (IQR) of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        tuple: The first quartile (Q1), third quartile (Q3), and the IQR.

    Example:
        >>> iqr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        (3.25, 7.75, 4.5)
    """
    if not data:
        raise ValueError("List is empty")
    
    # Ensure all elements in the list are numeric
    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("All elements in the data list must be numeric")
    
    sorted_data = sorted(data)
    Q1_index = int(0.25 * (len(sorted_data) - 1))
    Q3_index = int(0.75 * (len(sorted_data) - 1))
    
    Q1 = sorted_data[Q1_index]
    Q3 = sorted_data[Q3_index]
    return Q1, Q3, Q3 - Q1
