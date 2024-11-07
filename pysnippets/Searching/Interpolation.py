import logging
from typing import List

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def interpolation_search(arr: List[int], target: int) -> int:
    """Interpolation search algorithm.
    Args:
        arr (List[int]): Sorted list of elements to search through (with uniformly distributed values).
        target (int): The element to search for.
    Returns:
        int: The index of the target if found, else -1.
    """
    logging.info("Starting interpolation search")
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                logging.info(f"Target {target} found at index {low}")
                return low
            logging.warning(f"Target {target} not found in array.")
            return -1
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        logging.debug(f"Interpolated position: {pos}")
        if arr[pos] == target:
            logging.info(f"Target {target} found at index {pos}")
            return pos
        if arr[pos] < target:
            low = pos + 1
            logging.debug(f"Target greater than {arr[pos]}, new low={low}")
        else:
            high = pos - 1
            logging.debug(f"Target less than {arr[pos]}, new high={high}")
    logging.warning(f"Element {target} is not present in array")
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = interpolation_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")
