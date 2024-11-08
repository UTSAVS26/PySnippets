import logging
from typing import List, Any

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def cocktail_shaker_sort(arr: List[Any]) -> List[Any]:
    """
    Sorts an array using the Cocktail Shaker Sort algorithm.

    Args:
        arr (List[Any]): The list of elements to be sorted.

    Returns:
        List[Any]: The sorted list.

    Raises:
        TypeError: If arr is not a list.

    Time Complexity:
        Worst and Average Case: O(n^2)
        Best Case: O(n) if the list is already sorted.
    """
    if not isinstance(arr, list):
        logging.error("Input must be a list.")
        raise TypeError("arr must be a list.")

    n = len(arr)
    logging.debug(f"Starting Cocktail Shaker Sort with n={n}")

    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                logging.debug(f"Swapping indices {i} and {i + 1}: {arr[i]} <-> {arr[i + 1]}")
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            logging.debug("No swaps made in the forward pass, list might be sorted already.")
            break

        end -= 1
        swapped = False

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                logging.debug(f"Swapping indices {i - 1} and {i}: {arr[i - 1]} <-> {arr[i]}")
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        if not swapped:
            logging.debug("No swaps made in the backward pass, list might be sorted already.")

        start += 1

    logging.info("Cocktail Shaker Sort completed.")
    return arr

# Example usage:
if __name__ == "__main__":
    sample_list = [5, 3, 8, 4, 2]
    sorted_list = cocktail_shaker_sort(sample_list)
    print("Sorted List:", sorted_list)