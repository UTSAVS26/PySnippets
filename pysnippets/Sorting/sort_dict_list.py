import logging
from typing import List, Dict, Any

from .bubble_sort import bubble_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort
from .cocktail_sort import cocktail_sort

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def validate_key_in_dict_list(dict_list: List[Dict[str, Any]], key: str) -> bool:
    """Validate that the key exists in all dictionaries and that key values are of valid types."""
    if not all(key in d for d in dict_list):
        logging.error(f"The key '{key}' is not present in all dictionaries.")
        raise ValueError(f"The key '{key}' is not present in all dictionaries.")
    
    # Ensure that the key values are strings or integers (you can extend this validation)
    if not all(isinstance(d[key], (str, int)) for d in dict_list):
        logging.error(f"Key values must be either strings or integers, but got other types.")
        raise ValueError(f"Key values must be either strings or integers, but got other types.")
    
    return True

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
        ValueError: If the list is empty, the key is not present, or an unsupported sorting method is specified.
    """
    
    # Validate that the list is not empty and the key exists in all dictionaries
    if not dict_list:
        logging.error("The list of dictionaries is empty.")
        raise ValueError("The list of dictionaries is empty.")
    
    # Validate key presence and type
    validate_key_in_dict_list(dict_list, key)

    logging.debug(f"Sorting using method: {method}")

    # Create a copy of the list to avoid modifying the original
    dict_list_copy = dict_list[:]

    # Choose the sorting method
    if method == "bubble":
        sorted_list = bubble_sort(dict_list_copy, key, reverse)
    elif method == "insertion":
        sorted_list = insertion_sort(dict_list_copy, key, reverse)
    elif method == "merge":
        sorted_list = merge_sort(dict_list_copy, key)
    elif method == "quick":
        sorted_list = quick_sort(dict_list_copy, key)
    elif method == "cocktail":
        sorted_list = cocktail_sort(dict_list_copy, key, reverse)
    else:
        logging.error(f"Unsupported sorting method: {method}")
        raise ValueError(f"Unsupported sorting method: {method}")
    
    logging.info(f"Sorting completed using {method} sort.")

    # Log the sorted list
    logging.debug(f"Sorted list: {sorted_list}")

    return sorted_list

# Example usage:
if __name__ == "__main__":
    dict_list = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "David", "age": 20}
    ]

    # Example of sorting by 'age' in descending order using 'quick' sort
    sorted_list = sort_dict_list(dict_list, key="age", method="quick", reverse=True)
    print(f"Sorted by age (desc): {sorted_list}")

    # Example of sorting by 'name' using 'merge' sort
    sorted_list = sort_dict_list(dict_list, key="name", method="merge")
    print(f"Sorted by name: {sorted_list}")