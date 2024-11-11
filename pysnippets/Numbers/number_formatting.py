# number_formatting.py


def format_number(num: float, thousands_sep: str = ',', decimal_sep: str = '.') -> str:
    """
    Format a number with commas as thousand separators.

    Args:
        num (int, float): The number to format.

    Returns:
        str: The formatted number as a string.
    """
    if not isinstance(num, (int, float)):
        raise ValueError("The input should be an integer or a float.")
    
    formatted_num = f"{num:,}".replace(',', thousands_sep).replace('.', decimal_sep)
    return formatted_num


# Example usage
if __name__ == "__main__":
    print(format_number(1234567)) # Output: "1,234,567"
    print(format_number(12345.6789, thousands_sep=' ', decimal_sep=',')) #output: 12 345,6789
    print(format_number(-1234567.89))
    print(format_number(1234567.89, ".", ','))
     
