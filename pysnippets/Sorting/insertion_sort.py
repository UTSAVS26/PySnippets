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

def insertion_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    try:
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")
        
        if not all(isinstance(item[key], (int, float, str)) for item in dict_list):
            logging.error(f"Invalid type for key '{key}' in dictionaries. Must be int, float, or string.")
            raise TypeError(f"Key '{key}' must have a valid comparable type (int, float, string).")
        
        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")
        
        logging.debug(f"Starting Insertion Sort with n={len(dict_list)}, key='{key}', reverse={reverse}")
        
        if not dict_list:
            logging.info("Empty list provided. Returning empty list.")
            return []
    
        for i in range(1, len(dict_list)):
            key_item = dict_list[i]
            j = i - 1
            
            while j >= 0 and (key_item[key] < dict_list[j][key]) != reverse:
                logging.debug(f"Shifting index {j} to {j + 1}: {dict_list[j]} -> {key_item}")
                dict_list[j + 1] = dict_list[j]
                j -= 1
                
            dict_list[j + 1] = key_item
        
        logging.info("Insertion Sort completed.")
        return dict_list

    except Exception as e:
        logging.error(f"An error occurred during Insertion Sort: {e}")
        raise
