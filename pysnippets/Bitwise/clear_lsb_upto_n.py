def clear_lsb_up_to_pos(n, pos):
    """Clears all least significant bits up to a given position using bitwise operations for efficiency."""
    return n & ~((1 << pos) - 1)  # Clear LSBs up to pos using bitwise operations
