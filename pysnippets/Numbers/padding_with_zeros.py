
# padding_with_zeros.py

def pad_with_zeros(num, total_length):
    """
    Pad a number with leading zeros to achieve a specified total length.

    Args:
        num (int, float): The number to pad with zeros.
        total_length (int): The total length of the final string.

    Returns:
        str: The number padded with zeros.

    Example:
        >>> pad_with_zeros(42, 5)
        '00042'
    """
    return f"{num:0{total_length}}"


# Example usage
if __name__ == "__main__":
    print(pad_with_zeros(42, 5))  # Output: "00042"
