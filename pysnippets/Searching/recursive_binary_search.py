import logging
from typing import List

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def binary_search_recursive(arr: List[int], low: int, high: int, target: int) -> int:
    """
    Perform a recursive binary search on a sorted array.

    Args:
        arr (List[int]): A sorted list of elements to search in.
        low (int): The starting index of the subarray to search.
        high (int): The ending index of the subarray to search.
        target (int): The element to search for.

    Returns:
        int: The index of the target if found; otherwise, -1.
    """
    logging.debug(f"Binary search recursive called with low={low}, high={high}")

    if high >= low:
        mid = low + (high - low) // 2
        logging.debug(f"Checking middle index {mid}, value={arr[mid]}")

        if arr[mid] == target:
            logging.info(f"Target {target} found at index {mid}")
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, low, mid - 1, target)
        else:
            return binary_search_recursive(arr, mid + 1, high, target)

    logging.warning(f"Element {target} is not present in array")
    return -1

# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    target = 10

    # Function call
    result = binary_search_recursive(arr, 0, len(arr) - 1, target)

    if result != -1:
        logging.info(f"Element is present at index {result}")
    else:
        logging.info("Element is not present in array")
