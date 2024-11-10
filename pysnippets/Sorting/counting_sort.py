import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: int
    value: Dict[str, Any]

def counting_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Counting Sort algorithm based on a specified key.
    """
    try:
        if not dict_list:
            logging.info("Empty list provided. Returning empty list.")
            return []
    
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")
    
        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")
    
        if not all(isinstance(item[key], int) and item[key] >= 0 for item in dict_list):
            logging.error("All key values must be non-negative integers for Counting Sort.")
            raise ValueError("All key values must be non-negative integers for Counting Sort.")
    
        logging.debug(f"Starting Counting Sort with n={len(dict_list)}, key='{key}', reverse={reverse}")
    
        max_val = max(item[key] for item in dict_list)
        count = [0] * (max_val + 1)
        output = [None] * len(dict_list)
    
        for item in dict_list:
            count[item[key]] += 1
    
        logging.debug(f"Count array: {count}")
    
        for i in range(1, len(count)):
            count[i] += count[i - 1]
    
        logging.debug(f"Modified count array: {count}")
    
        for item in reversed(dict_list):
            position = count[item[key]] - 1
            output[position] = item
            count[item[key]] -= 1
    
        if reverse:
            logging.debug("Reversing the sorted list for descending order.")
            output.reverse()
    
        logging.info("Counting Sort completed.")
        return output
    
    except Exception as e:
        logging.error(f"An error occurred during Counting Sort: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    dict_list = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
    sorted_list = counting_sort(dict_list, key="age", reverse=True)
    print("Sorted List:", sorted_list)
