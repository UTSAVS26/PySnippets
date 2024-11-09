import logging
from typing import List, Optional

# Configure logging to show detailed information during search
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def interpolation_search(arr: List[int], target: int) -> int:
    """
    Interpolation search algorithm for sorted, uniformly distributed arrays.
    
    Args:
        arr (List[int]): Sorted list of integers to search through.
        target (int): The element to search for in the list.
        
    Returns:
        int: The index of the target if found, else -1.
    """
    logging.info("Starting interpolation search")
    if not arr:
        logging.warning("Empty array provided.")
        return -1
    
    low, high = 0, len(arr) - 1
    
    # While range is valid and target is within the bounds
    while low <= high and arr[low] <= target <= arr[high]:
        # Check for zero division edge case
        if arr[high] == arr[low]:
            if arr[low] == target:
                logging.info(f"Target {target} found at index {low}")
                return low
            logging.warning(f"Target {target} not found in the array.")
            return -1

        # Estimate position of the target based on interpolation
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        logging.debug(f"Interpolated position: {pos}")

        # Compare the target with the element at interpolated position
        if arr[pos] == target:
            logging.info(f"Target {target} found at index {pos}")
            return pos
        elif arr[pos] < target:
            low = pos + 1
            logging.debug(f"Target greater than {arr[pos]}, new low={low}")
        else:
            high = pos - 1
            logging.debug(f"Target less than {arr[pos]}, new high={high}")

    logging.warning(f"Element {target} is not present in array")
    return -1

# Driver Code and Additional Test Cases
if __name__ == "__main__":
    # Initial test case
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = interpolation_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")

    # Additional test cases
    test_cases = [
        {"arr": [1, 2, 3, 4, 5], "target": 4, "expected": 3},
        {"arr": [10, 20, 30, 40, 50], "target": 25, "expected": -1},
        {"arr": [15, 15, 15, 15, 15], "target": 15, "expected": 0},  # Test for all identical elements
        {"arr": [], "target": 7, "expected": -1},                   # Test for empty array
        {"arr": [3, 6, 8, 12, 14, 17], "target": 12, "expected": 3}, # Standard case
    ]

    for idx, case in enumerate(test_cases, 1):
        arr, target, expected = case["arr"], case["target"], case["expected"]
        result = interpolation_search(arr, target)
        assert result == expected, f"Test case {idx} failed: expected {expected}, got {result}"
        logging.info(f"Test case {idx} passed.")