from typing import List, Any


def flatten(nested_list: List[Any]) -> List[Any]:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
