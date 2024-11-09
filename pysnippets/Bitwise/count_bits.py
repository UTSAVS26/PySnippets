def count_set_bits(n):
    """Counts the number of set bits (1s) in an integer n using a more efficient approach."""
    count = 0
    while n:
        count += n & 1  # Increment count if the least significant bit is 1
        n >>= 1  # Right shift n to process the next bit
    return count
