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


def cocktail_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False, case_sensitive: bool = True) -> List[Dict[str, Any]]:
    try:
        if not isinstance(dict_list, list) or not all(isinstance(item, dict) for item in dict_list):
            logging.error("Input must be a list of dictionaries.")
            raise TypeError("dict_list must be a list of dictionaries.")

        if not isinstance(key, str):
            logging.error(f"Provided key '{key}' is not a string.")
            raise TypeError("The key must be a string.")

        if not all(key in item for item in dict_list):
            logging.error(f"The key '{key}' is not present in all dictionaries.")
            raise KeyError(f"The key '{key}' is not present in all dictionaries.")

        n = len(dict_list)
        start = 0
        end = n - 1
        logging.debug(f"Starting Cocktail Sort with n={n}, key='{key}', reverse={reverse}, case_sensitive={case_sensitive}")

        def get_normalized_key(item):
            value = item[key]
            if isinstance(value, str) and not case_sensitive:
                return value.lower()
            return value

        while start < end:
            swapped = False
            new_end = start
            for i in range(start, end):
                if (get_normalized_key(dict_list[i]) > get_normalized_key(dict_list[i + 1])) != reverse:
                    logging.debug(f"Swapping indices {i} and {i + 1}: {dict_list[i]} <-> {dict_list[i + 1]}")
                    dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                    swapped = True
                    new_end = i
            end = new_end

            if not swapped:
                logging.debug("No swaps made during forward pass, list might be sorted already.")
                break

            swapped = False
            new_start = end
            for i in range(end - 1, start - 1, -1):
                if (get_normalized_key(dict_list[i]) > get_normalized_key(dict_list[i + 1])) != reverse:
                    logging.debug(f"Swapping indices {i} and {i + 1}: {dict_list[i]} <-> {dict_list[i + 1]}")
                    dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                    swapped = True
                    new_start = i
            start = new_start

            if not swapped:
                logging.debug("No swaps made during backward pass, list might be sorted already.")
                break

        logging.info("Cocktail Sort completed.")
        return dict_list

    except Exception as e:
        logging.error(f"An error occurred during Cocktail Sort: {e}")
        raise
