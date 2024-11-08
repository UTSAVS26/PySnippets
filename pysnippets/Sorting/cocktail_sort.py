import logging
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def cocktail_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Cocktail Sort algorithm based on a specified key.
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
    n = len(dict_list)
    start = 0
    end = n - 1
    logging.debug(f"Starting Cocktail Sort with n={n}, key='{key}', reverse={reverse}")
    while start < end:
        new_end = start
        for i in range(start, end):
            if (dict_list[i][key] > dict_list[i + 1][key]) != reverse:
                logging.debug(f"Swapping indices {i} and {i + 1}: {dict_list[i]} <-> {dict_list[i + 1]}")
                dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                new_end = i
        end = new_end
        new_start = end
        for i in range(end - 1, start - 1, -1):
            if (dict_list[i][key] > dict_list[i + 1][key]) != reverse:
                logging.debug(f"Swapping indices {i} and {i + 1}: {dict_list[i]} <-> {dict_list[i + 1]}")
                dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                new_start = i
        start = new_start
    logging.info("Cocktail Sort completed.")
    return dict_list
