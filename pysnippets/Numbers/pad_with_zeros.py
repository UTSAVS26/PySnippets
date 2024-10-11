
def pad_with_zeros(num, width):
    """
    Pad a number with leading zeros to a specified width.

    Args:
        num (int): The number to pad.
        width (int): The total width of the output string.

    Returns:
        str: The number padded with leading zeros.
    """
    return str(num).zfill(width)
