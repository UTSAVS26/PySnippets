import logging
from typing import List

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def ternary_search(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
    """Ternary search algorithm.

    Args:
        arr (List[int]): Sorted list of elements to search through.
        target (int): The element to search for.
        left (int, optional): Left boundary for the search. Defaults to 0.
        right (int, optional): Right boundary for the search. Defaults to None.

    Returns:
        int: The index of the target if found, else -1.
    """
    if right is None:
        right = len(arr) - 1

    logging.info(f"Starting ternary search between indices {left} and {right}")
    if left > right:
        logging.warning(f"Element {target} is not present in array")
        return -1

    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    logging.debug(f"Calculated mid1={mid1}, mid2={mid2}")

    if arr[mid1] == target:
        logging.info(f"Target {target} found at index {mid1}")
        return mid1
    if arr[mid2] == target:
        logging.info(f"Target {target} found at index {mid2}")

    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = ternary_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")

