import logging
from typing import List

logging.basicConfig(
    level=logging.DEBUG,
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

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = exponential_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")
