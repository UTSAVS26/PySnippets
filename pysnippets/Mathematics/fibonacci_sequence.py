import logging
from typing import List, Union

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci_sequence(count: Union[int, None] = None, max_value: Union[int, None] = None) -> List[int]:
    """
    Generate a Fibonacci sequence up to a specified count or maximum value.

    Args:
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.

    Returns:
        list: List of Fibonacci numbers.
    """
    if count is None and max_value is None:
        raise ValueError("Either 'count' or 'max_value' must be provided.")

    if count is not None and count <= 0:
        raise ValueError("'count' must be a positive integer.")

    if max_value is not None and max_value < 0:
        raise ValueError("'max_value' must be a non-negative integer.")

    sequence = []
    a, b = 0, 1

    while (count is None or len(sequence) < count) and (max_value is None or a <= max_value):
        sequence.append(a)
        a, b = b, a + b

    logging.debug(f"Generated Fibonacci sequence: {sequence}")
    return sequence

# Example usage
if __name__ == "__main__":
    print(fibonacci_sequence(count=10)) 