import logging
from typing import List

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fibonacci_search(arr: List[int], target: int) -> int:
    """
    Fibonacci search algorithm.
    Args:
        arr (List[int]): Sorted list of elements to search through.
        target (int): The element to search for.
    Returns:
        int: The index of the element if found, else -1.
    """
    logging.info("Starting Fibonacci search")
    if not arr:
        logging.warning("Empty array provided.")
        return -1

    n = len(arr)
    fib_mm2, fib_mm1, fib_m = 0, 1, 1

    # Initialize Fibonacci numbers to find the smallest `fib_m` >= `n`
    while fib_m < n:
        fib_mm2, fib_mm1, fib_m = fib_mm1, fib_m, fib_mm2 + fib_mm1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_mm2, n - 1)
        logging.debug(f"Checking index {i}")

        if arr[i] < target:
            fib_m, fib_mm1, fib_mm2, offset = fib_mm1, fib_mm2, fib_m - fib_mm1, i
            logging.debug(f"Element {arr[i]} is less than target. New offset: {offset}")
        elif arr[i] > target:
            fib_m, fib_mm1, fib_mm2 = fib_mm2, fib_mm1 - fib_mm2, fib_m - fib_mm1
            logging.debug(f"Element {arr[i]} is greater than target.")
        else:
            logging.info(f"Target {target} found at index {i}")
            return i

    if fib_mm1 and offset + 1 < n and arr[offset + 1] == target:
        logging.info(f"Target {target} found at index {offset + 1}")
        return offset + 1

    logging.warning(f"Target {target} not found in the array.")
    return -1

# Driver Code and Unit Tests
if __name__ == "__main__":
    # Example test case
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = fibonacci_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

    # Additional test cases
    test_cases = [
        {"arr": [1, 3, 5, 7, 9], "target": 7, "expected": 3},
        {"arr": [1, 3, 5, 7, 9], "target": 6, "expected": -1},
        {"arr": [], "target": 10, "expected": -1},
        {"arr": [2, 4, 6, 8, 10, 12], "target": 8, "expected": 3},
        {"arr": [1, 3, 5, 7, 9, 11], "target": 1, "expected": 0}
    ]

    for idx, case in enumerate(test_cases, 1):
        arr, target, expected = case["arr"], case["target"], case["expected"]
        result = fibonacci_search(arr, target)
        assert result == expected, f"Test case {idx} failed: expected {expected}, got {result}"
        logging.info(f"Test case {idx} passed.")