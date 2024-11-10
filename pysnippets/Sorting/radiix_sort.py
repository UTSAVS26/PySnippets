import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def radix_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False) -> List[Dict[str, Any]]:
    try:
        if not dict_list:
            logging.info("Empty list provided. Returning empty list.")
            return []
        if not all(isinstance(item, dict) for item in dict_list):
            logging.error("All items must be dictionaries.")
            raise TypeError("All items must be dictionaries.")
        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")
        if not all(isinstance(item[key], int) and item[key] >= 0 for item in dict_list):
            logging.error("All key values must be non-negative integers for Radix Sort.")
            raise ValueError("All key values must be non-negative integers for Radix Sort.")

        max_key = max(item[key] for item in dict_list)
        exp = 1
        sorted_list = dict_list.copy()
        logging.debug(f"Maximum key value: {max_key}")

        while max_key // exp > 0:
            logging.debug(f"Sorting by exponent: {exp}")
            count = [0] * 10
            output = [None] * len(sorted_list)

            for item in sorted_list:
                index = (item[key] // exp) % 10
                count[index] += 1

            if reverse:
                for i in range(8, -1, -1):
                    count[i] += count[i + 1]
            else:
                for i in range(1, 10):
                    count[i] += count[i - 1]

            for i in range(len(sorted_list) - 1, -1, -1):
                index = (sorted_list[i][key] // exp) % 10
                output[count[index] - 1] = sorted_list[i]
                count[index] -= 1

            sorted_list = output
            logging.debug(f"List after sorting by exponent {exp}: {sorted_list}")
            exp *= 10

        if reverse:
            sorted_list.reverse()

        logging.info("Radix Sort completed.")
        return sorted_list

    except Exception as e:
        logging.error(f"An error occurred during Radix Sort: {e}")
        raise 