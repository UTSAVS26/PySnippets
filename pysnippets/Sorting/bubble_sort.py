import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def bubble_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Bubble Sort algorithm based on a specified key.

    Args:
        dict_list (List[Dict[str, Any]]): The list of dictionaries to sort.
        key (str): The key within the dictionaries to sort by.
        reverse (bool, optional): If True, sort in descending order. Defaults to False.

    Returns:
        List[Dict[str, Any]]: The sorted list of dictionaries.

    Raises:
        KeyError: If the specified key is not present in any of the dictionaries.
        TypeError: If dict_list is not a list of dictionaries.

    Time Complexity:
        Worst and Average Case: O(n^2)
        Best Case: O(n) if the list is already sorted.
    """
    if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
        logging.error("Input must be a list of dictionaries.")
        raise TypeError("dict_list must be a list of dictionaries.")

    if not all(key in item for item in dict_list):
        logging.error(f"The key '{key}' is not present in all dictionaries.")
        raise KeyError(f"The key '{key}' is not present in all dictionaries.")

    n = len(dict_list)
    logging.debug(f"Starting Bubble Sort with n={n}, key='{key}', reverse={reverse}")

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if (dict_list[j][key] > dict_list[j + 1][key]) != reverse:
                logging.debug(f"Swapping indices {j} and {j + 1}: {dict_list[j]} <-> {dict_list[j + 1]}")
                dict_list[j], dict_list[j + 1] = dict_list[j + 1], dict_list[j]
                swapped = True
        # If no two elements were swapped by the inner loop, the list is already sorted
        if not swapped:
            logging.debug("No swaps made, the list is already sorted.")
            break

    logging.info("Bubble Sort completed.")
    return dict_list