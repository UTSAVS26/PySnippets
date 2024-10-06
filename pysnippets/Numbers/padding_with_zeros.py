
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

# test_padding_with_zeros.py

from Padding_with_zeros import pad_with_zeros

def test_pad_with_zeros():
    assert pad_with_zeros(42, 5) == '00042'
    assert pad_with_zeros(123, 6) == '000123'
    assert pad_with_zeros(7, 2) == '07'
    assert pad_with_zeros(0, 3) == '000'
    assert pad_with_zeros(-5, 4) == '-05'
    print("All tests for pad_with_zeros passed!")

if __name__ == "__main__":
    test_pad_with_zeros()

