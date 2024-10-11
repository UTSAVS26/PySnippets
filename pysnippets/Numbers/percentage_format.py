
def percentage_format(num, total, decimals=2):
    """
    Format a number as a percentage of a total with specified decimal places.

    Args:
        num (float or int): The part value.
        total (float or int): The total value.
        decimals (int): Number of decimal places.

    Returns:
        str: The percentage formatted as a string.
    """
    if total == 0:
        raise ValueError("Total must not be zero.")
    percentage = (num / total) * 100
    return f"{percentage:.{decimals}f}%"
