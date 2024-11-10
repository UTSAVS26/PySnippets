import logging
from typing import List, Dict, Any
from dataclasses import dataclass
import random

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def quick_sort(dict_list: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Quick Sort algorithm based on a specified key.
    """
    try:
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")
        
        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")
        
        logging.debug(f"Starting Quick Sort with n={len(dict_list)}, key='{key}'")
        
        if len(dict_list) <= 1:
            return dict_list
        
        pivot = random.choice(dict_list)[key]
        logging.debug(f"Pivot chosen: {pivot}")
        
        left = [x for x in dict_list if x[key] < pivot]
        middle = [x for x in dict_list if x[key] == pivot]
        right = [x for x in dict_list if x[key] > pivot]
        
        logging.debug(f"Left partition: {left}")
        logging.debug(f"Middle partition: {middle}")
        logging.debug(f"Right partition: {right}")
        
        return quick_sort(left, key) + middle + quick_sort(right, key)
    
    except Exception as e:
        logging.error(f"An error occurred during Quick Sort: {e}")
        raise
