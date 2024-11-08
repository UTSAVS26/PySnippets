import logging

from typing import List, Dict, Any

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def heap_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Heap Sort algorithm based on a specified key.

    Args:
        dict_list (List[Dict[str, Any]]): The list of dictionaries to sort.
        key (str): The key within the dictionaries to sort by.
        reverse (bool, optional): If True, sort in descending order. Defaults to False.

    Returns:
        List[Dict[str, Any]]: The sorted list of dictionaries.

    Raises:
        KeyError: If the specified key is not present in any of the dictionaries.
        TypeError: If dict_list is not a list of dictionaries.
    """
    if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
        logging.error("Input must be a list of dictionaries.")
        raise TypeError("dict_list must be a list of dictionaries.")

    if not all(key in item for item in dict_list):
        logging.error(f"The key '{key}' is not present in all dictionaries.")
        raise KeyError(f"The key '{key}' is not present in all dictionaries.")

    def heapify(lst, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and (lst[left][key] > lst[largest][key]) != reverse:
            largest = left

        if right < n and (lst[right][key] > lst[largest][key]) != reverse:
            largest = right

        if largest != i:
            logging.debug(f"Swapping indices {i} and {largest}: {lst[i]} <-> {lst[largest]}")
            lst[i], lst[largest] = lst[largest], lst[i]
            heapify(lst, n, largest)

    n = len(dict_list)
    logging.debug(f"Starting Heap Sort with n={n}, key='{key}', reverse={reverse}")

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(dict_list, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        logging.debug(f"Swapping root with index {i}: {dict_list[0]} <-> {dict_list[i]}")
        dict_list[i], dict_list[0] = dict_list[0], dict_list[i]
        heapify(dict_list, i, 0)

    logging.info("Heap Sort completed.")
    return dict_list
