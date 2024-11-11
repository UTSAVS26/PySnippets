import logging
from typing import List

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def linear_search(arr: List[int], target: int) -> int:
    """
    Executes a linear search on a list to find a target element.

    Args:
        arr (List[int]): The list of elements to search through.
        target (int): The element to search for within the list.

    Returns:
        int: The index of the target element if found; otherwise, -1.
    """
    if not arr:  # Check for empty array
        logging.error("The provided list is empty.")
        return -1

    for index, element in enumerate(arr):
        logging.debug(f"Checking index {index}, value {element}")
        if element == target:
            logging.info(f"Target {target} found at index {index}")
            return index

    logging.warning(f"Target {target} not found in the list.")
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10

    result = linear_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print(f"Element is present at index {result}")