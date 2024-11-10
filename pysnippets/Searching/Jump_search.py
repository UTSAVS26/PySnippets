import logging
import math
from typing import List

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def jump_search(arr: List[int], target: int) -> int:
    """
    Jump search algorithm.
    
    Args:
        arr (List[int]): Sorted list of elements to search through.
        target (int): The element to search for.
    
    Returns:
        int: The index of the target if found, else -1.
    """
    logging.info("Starting jump search")
    if not arr:
        logging.error("Empty array provided for search.")
        return -1
    
    n = len(arr)
    step = int(math.sqrt(n))  # Step size is the square root of the array length
    prev = 0

    # Jump to the right block
    while prev < n and arr[min(step, n) - 1] < target:
        logging.debug(f"Jumping from index {prev} to index {step}")
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            logging.warning(f"Element {target} is not present in array")
            return -1
    
    # Perform a linear search within the found block
    for i in range(prev, min(step, n)):
        logging.debug(f"Checking index {i}, value={arr[i]}")
        if arr[i] == target:
            logging.info(f"Target {target} found at index {i}")
            return i

    logging.warning(f"Element {target} is not present in array")
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = jump_search(arr, target)
    if result == -1:
        logging.info("Element is not present in array")
    else:
        logging.info(f"Element is present at index {result}")