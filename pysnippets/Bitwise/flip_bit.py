def flip_bit(n, pos):
    """Flips the bit at the specified position in n using bitwise XOR."""
    return n ^ (1 << pos)  # Flip the bit at position pos
