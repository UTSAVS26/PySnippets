import logging

from typing import List, Dict, Any

from .bubble_sort import bubble_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort
from .cocktail_sort import cocktail_sort

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def sort_dict_list(dict_list: List[Dict[str, Any]], key: str, method: str = "quick", reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries by a specified key using the chosen sorting algorithm.

    Args:
        dict_list (List[Dict[str, Any]]): A list of dictionaries to be sorted.
        key (str): The dictionary key to sort by.
        method (str, optional): The sorting algorithm to use ('bubble', 'insertion', 'merge', 'quick', 'cocktail'). Defaults to 'quick'.
        reverse (bool, optional): If True, sort in descending order. Defaults to False.

    Returns:
        List[Dict[str, Any]]: A new list of dictionaries sorted by the specified key.

    Raises:
        ValueError: If the list is empty or if the specified key is not present in all dictionaries.
        ValueError: If an unsupported sorting method is specified.
    """

    if not dict_list:
        logging.error("The list of dictionaries is empty.")
        raise ValueError("The list of dictionaries is empty.")

    if not all(key in d for d in dict_list):
        logging.error(f"The key '{key}' is not present in all dictionaries.")
        raise ValueError(f"The key '{key}' is not present in all dictionaries.")

    logging.debug(f"Sorting using method: {method}")

    if method == "bubble":
        return bubble_sort(dict_list, key, reverse)
    elif method == "insertion":
        return insertion_sort(dict_list, key, reverse)
    elif method == "merge":
        return merge_sort(dict_list, key)
    elif method == "quick":
        return quick_sort(dict_list, key)
    elif method == "cocktail":
        return cocktail_sort(dict_list, key, reverse)
    else:
        logging.error(f"Unsupported sorting method: {method}")
        raise ValueError(f"Unsupported sorting method: {method}")
