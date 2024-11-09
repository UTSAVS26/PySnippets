import logging
from typing import List, Dict, Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def insertion_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Insertion Sort algorithm based on a specified key.
    
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
    
    if not all(isinstance(item[key], (int, float, str)) for item in dict_list):  # Ensure valid type for sorting
        logging.error(f"Invalid type for key '{key}' in dictionaries. Must be int, float, or string.")
        raise TypeError(f"Key '{key}' must have a valid comparable type (int, float, string).")
    
    if not all(key in item for item in dict_list):
        logging.error(f"The key '{key}' is not present in all dictionaries.")
        raise KeyError(f"The key '{key}' is not present in all dictionaries.")
    
    logging.debug(f"Starting Insertion Sort with n={len(dict_list)}, key='{key}', reverse={reverse}")
    
    # Handle empty list case
    if not dict_list:
        logging.info("Empty list provided. Returning empty list.")
        return []

    for i in range(1, len(dict_list)):
        key_item = dict_list[i]
        j = i - 1
        
        # Shift elements to the right until we find the correct position for key_item
        while j >= 0 and (key_item[key] < dict_list[j][key]) != reverse:
            logging.debug(f"Shifting index {j} to {j + 1}: {dict_list[j]} -> {key_item}")
            dict_list[j + 1] = dict_list[j]
            j -= 1
            
        dict_list[j + 1] = key_item
    
    logging.info("Insertion Sort completed.")
    return dict_list