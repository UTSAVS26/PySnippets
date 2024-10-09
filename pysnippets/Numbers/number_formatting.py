# number_formatting.py


def format_number(num: float, thousands_sep: str = ',', decimal_sep: str='.') -> str:
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
    if not isinstance(num,(int, float)):
        raise ValueError("The Input should be integer or a float.")
    
    formatted_num = f"{num:,}"

    if thousands_sep != ',' or decimal_sep != '.':
        formatted_num = formatted_num.replace(',', thousands_sep).replace('.', decimal_sep)

    return formatted_num


# Example usage
if __name__ == "__main__":
    print(format_number(1234567)) # Output: "1,234,567"
    print(format_number(12345.6789, thousands_sep=' ', decimal_sep=',')) #output: 12 345,6789
    print(format_number(-1234567.89))
    print(format_number(1234567.89, ".", ','))
     
