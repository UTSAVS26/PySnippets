import logging
from typing import List, Dict, Any
from dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class SortItem:
    key: Any
    value: Dict[str, Any]

def bucket_sort(dict_list: List[Dict[str, Any]], key: str, reverse: bool = False, bucket_size: int = 5) -> List[Dict[str, Any]]:
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
        if not all(isinstance(item[key], (int, float)) for item in dict_list):
            logging.error("All key values must be integers or floats for Bucket Sort.")
            raise ValueError("All key values must be integers or floats for Bucket Sort.")

        min_key = min(item[key] for item in dict_list)
        max_key = max(item[key] for item in dict_list)
        bucket_count = int((max_key - min_key) // bucket_size + 1)
        buckets = [[] for _ in range(bucket_count)]

        for item in dict_list:
            index = (item[key] - min_key) // bucket_size
            buckets[int(index)].append(item)

        sorted_list = []
        for bucket in buckets:
            if bucket:
                bucket_sorted = sorted(bucket, key=lambda x: x[key], reverse=reverse)
                sorted_list.extend(bucket_sorted)

        if reverse:
            sorted_list.reverse()

        logging.info("Bucket Sort completed.")
        return sorted_list

    except Exception as e:
        logging.error(f"An error occurred during Bucket Sort: {e}")
        raise 