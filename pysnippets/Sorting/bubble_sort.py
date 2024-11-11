import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def bubble_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    try:
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")

        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")

        n = len(dict_list)
        logging.debug(f"Starting Bubble Sort with n={n}, key='{key}', reverse={reverse}")

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if (dict_list[j][key] > dict_list[j + 1][key]) != reverse:
                    logging.debug(f"Swapping indices {j} and {j + 1}: {dict_list[j]} <-> {dict_list[j + 1]}")
                    dict_list[j], dict_list[j + 1] = dict_list[j + 1], dict_list[j]
                    swapped = True
            if not swapped:
                logging.debug("No swaps made, the list is already sorted.")
                break

        logging.info("Bubble Sort completed.")
        return dict_list

    except Exception as e:
        logging.error(f"An error occurred during Bubble Sort: {e}")
        raise