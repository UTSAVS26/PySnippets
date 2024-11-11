import logging
from typing import List

# Parameterized logging configuration
def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def binary_search(arr: List[int], target: int, low: int, high: int) -> int:
    """Perform a binary search on a sorted array.
    Args:
        arr (List[int]): Sorted list of elements to search through.
        target (int): The element to search for.
        low (int): Lower index of the search range.
        high (int): Higher index of the search range.
    Returns:
        int: The index of the target if found, else -1.
    """
    logging.debug(f"Binary search called with low={low}, high={high}")
    if high >= low:
        mid = (high + low) // 2
        logging.debug(f"Checking middle index {mid}")
        if arr[mid] == target:
            logging.info(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, high)
    logging.warning(f"Target {target} not found in the array.")
    return -1

def exponential_search(arr: List[int], target: int) -> int:
    """Exponential search algorithm.
    Args:
        arr (List[int]): Sorted list of elements to search through.
        target (int): The element to search for.
    Returns:
        int: The index of the target if found, else -1.
    """
    logging.info("Starting exponential search")
    if not arr:
        logging.error("Empty array provided for search.")
        return -1
    if arr[0] == target:
        logging.info("Target found at index 0")
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        logging.debug(f"Exponential search checking index {i}")
        i *= 2
    result = binary_search(arr, target, i // 2, min(i, n - 1))
    if result != -1:
        logging.info(f"Element {target} found at index {result}")
    else:
        logging.info(f"Element {target} is not present in array")
    return result

# Unit Tests for the Search Functions
def run_tests():
    test_cases = [
        {"arr": [2, 3, 4, 10, 40], "target": 10, "expected": 3},
        {"arr": [1, 2, 3, 4, 5], "target": 6, "expected": -1},
        {"arr": [1, 3, 5, 7, 9, 11], "target": 1, "expected": 0},
        {"arr": [], "target": 3, "expected": -1},
        {"arr": [2, 4, 6, 8, 10], "target": 8, "expected": 3},
    ]

    for i, test_case in enumerate(test_cases, 1):
        arr, target, expected = test_case["arr"], test_case["target"], test_case["expected"]
        result = exponential_search(arr, target)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        logging.info(f"Test case {i} passed.")

# Driver Code
if __name__ == "__main__":
    # Setup logging level
    setup_logging(level=logging.DEBUG)

    # Sample exponential search
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = exponential_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")

    # Run unit tests
    logging.info("Running unit tests...")
    run_tests()
    logging.info("All tests completed successfully.")