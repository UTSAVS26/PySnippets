
# Formatting to 2 decimal.py

def format_to_two_decimals(num):
    """
    Format a number to two decimal places.

    Args:
        num (float): The number to format.

    Returns:
        str: The formatted number as a string with two decimal places.

    Example:
        >>> format_to_two_decimals(1234.5678)
        '1234.57'
    """
    return f"{num:.2f}"


# Example usage
if __name__ == "__main__":
    print(format_to_two_decimals(1234.5678))  # Output: "1234.57"
