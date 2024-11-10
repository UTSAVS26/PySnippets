def find_unique(arr):
    """Finds the unique number in an array where every other number appears twice using XOR for efficiency."""
    unique = 0
    for num in arr:
        unique ^= num  # XOR all numbers; duplicates will cancel out
    return unique
