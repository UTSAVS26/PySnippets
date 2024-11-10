import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def merge_sort(dict_list: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Merge Sort algorithm based on a specified key.
    """
    try:
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")
    
        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")
        
        logging.debug(f"Starting Merge Sort with n={len(dict_list)}, key='{key}'")
    
        if len(dict_list) > 1:
            mid = len(dict_list) // 2
            left_half = dict_list[:mid]
            right_half = dict_list[mid:]
    
            logging.debug(f"Dividing list into left_half={left_half} and right_half={right_half}")
            
            merge_sort(left_half, key)
            merge_sort(right_half, key)
    
            i = j = k = 0
    
            while i < len(left_half) and j < len(right_half):
                if left_half[i][key] < right_half[j][key]:
                    dict_list[k] = left_half[i]
                    i += 1
                else:
                    dict_list[k] = right_half[j]
                    j += 1
                k += 1
    
            while i < len(left_half):
                dict_list[k] = left_half[i]
                i += 1
                k += 1
    
            while j < len(right_half):
                dict_list[k] = right_half[j]
                j += 1
                k += 1
    
        logging.info("Merge Sort completed.")
        return dict_list
    
    except Exception as e:
        logging.error(f"An error occurred during Merge Sort: {e}")
        raise
