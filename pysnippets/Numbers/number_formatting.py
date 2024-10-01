# number_formatting.py


def format_number(num):
    """
    Format a number with commas as thousand separators.

    Args:
        num (int, float): The number to format.

    Returns:
        str: The formatted number as a string.

    Example:
        >>> format_number(1234567)
        '1,234,567'
    """
    return f"{num:,}"


# Example usage
if __name__ == "__main__":
    print(format_number(1234567))  # Output: "1,234,567"
