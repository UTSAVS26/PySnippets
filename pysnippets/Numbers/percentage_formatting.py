
# percentage_formatting.py

def format_percentage(value, decimal_places=2):
    """
    Format a number as a percentage with a specified number of decimal places.

    Args:
        value (float): The number to format as a percentage.
        decimal_places (int): The number of decimal places (default is 2).

    Returns:
        str: The formatted percentage as a string.

    Example:
        >>> format_percentage(0.7567)
        '75.67%'
    """
    return f"{value * 100:.{decimal_places}f}%"


# Example usage
if __name__ == "__main__":
    print(format_percentage(0.7567))  # Output: "75.67%"
