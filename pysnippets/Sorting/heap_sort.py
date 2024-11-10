import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def heap_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries using the Heap Sort algorithm based on a specified key.
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
        
        def heapify(lst, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            compare = (lambda x, y: x > y) if not reverse else (lambda x, y: x < y)
    
            if left < n and compare(lst[left][key], lst[largest][key]):
                largest = left
    
            if right < n and compare(lst[right][key], lst[largest][key]):
                largest = right
    
            if largest != i:
                logging.debug(f"Swapping indices {i} and {largest}: {lst[i]} <-> {lst[largest]}")
                lst[i], lst[largest] = lst[largest], lst[i]
                heapify(lst, n, largest)
    
        n = len(dict_list)
        logging.debug(f"Starting Heap Sort with n={n}, key='{key}', reverse={reverse}")
    
        # Build a heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(dict_list, n, i)
    
        # Extract elements from heap
        for i in range(n - 1, 0, -1):
            logging.debug(f"Swapping root with index {i}: {dict_list[0]} <-> {dict_list[i]}")
            dict_list[i], dict_list[0] = dict_list[0], dict_list[i]
            heapify(dict_list, i, 0)
    
        logging.info("Heap Sort completed.")
        return dict_list
    
    except Exception as e:
        logging.error(f"An error occurred during Heap Sort: {e}")
        raise

# Example usage:
if __name__ == "__main__":
    dict_list = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]
    sorted_list = heap_sort(dict_list, key="age", reverse=True)
    print("Sorted List:", sorted_list)
