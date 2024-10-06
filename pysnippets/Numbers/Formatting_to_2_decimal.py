
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

# test_formatting_to_2_decimal.py

from Formatting_to_2_decimal import format_to_2_decimal

def test_format_to_2_decimal():
    assert format_to_2_decimal(3.14159) == '3.14'
    assert format_to_2_decimal(2.5) == '2.50'
    assert format_to_2_decimal(1.0) == '1.00'
    assert format_to_2_decimal(0) == '0.00'
    assert format_to_2_decimal(-2.345) == '-2.35'
    print("All tests for format_to_2_decimal passed!")

if __name__ == "__main__":
    test_format_to_2_decimal()

