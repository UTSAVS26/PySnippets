def is_power_of_two(n):
    """Checks if a number is a power of two using a bitwise trick."""
    return n > 0 and (n & (n - 1)) == 0  # A power of two has only one bit set
