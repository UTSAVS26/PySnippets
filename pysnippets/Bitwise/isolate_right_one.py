def isolate_rightmost_one(n):
    """Isolates the rightmost 1-bit in n using bitwise operations."""
    return n & -n  # Use two's complement to isolate the rightmost 1-bit
