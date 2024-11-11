def swap_numbers(a, b):
    """Swaps two numbers using XOR for efficiency."""
    a ^= b
    b ^= a
    a ^= b
    return a, b
