# dictionary_manipulation.py

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries into one. If keys are duplicated, values from dict2 will overwrite those from dict1.

    Example usage:
    merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) -> {'a': 1, 'b': 3, 'c': 4}
    """
    merged = dict1.copy()  # Create a copy of dict1
    merged.update(dict2)   # Update with dict2
    return merged

def filter_dict_by_value(d: dict, threshold: int) -> dict:
    """
    Filters the dictionary, returning only items where the value is above the given threshold.

    Example usage:
    filter_dict_by_value({'a': 1, 'b': 5, 'c': 3}, 2) -> {'b': 5, 'c': 3}
    """
    return {k: v for k, v in d.items() if v > threshold}

def get_keys_with_value(d: dict, target_value) -> list:
    """
    Returns a list of keys that have the specified value.

    Example usage:
    get_keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1) -> ['a', 'c']
    """
    return [k for k, v in d.items() if v == target_value]

def invert_dict(d: dict) -> dict:
    """
    Inverts a dictionary, swapping its keys and values. If there are duplicate values, only one will be kept.

    Example usage:
    invert_dict({'a': 1, 'b': 2, 'c': 1}) -> {1: 'c', 2: 'b'}
    """
    return {v: k for k, v in d.items()}

def dict_to_list(d: dict) -> list:
    """
    Converts a dictionary into a list of tuples (key, value).

    Example usage:
    dict_to_list({'a': 1, 'b': 2}) -> [('a', 1), ('b', 2)]
    """
    return list(d.items())

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_dict = {'a': 1, 'b': 2, 'c': 3}

    print("Original Dictionary:", sample_dict)
    print("Merged Dictionary:", merge_dicts({'a': 1}, {'b': 2}))
    print("Filtered Dictionary (values > 1):", filter_dict_by_value(sample_dict, 1))
    print("Keys with value 2:", get_keys_with_value(sample_dict, 2))
    print("Inverted Dictionary:", invert_dict({'a': 1, 'b': 2, 'c': 1}))
    print("Dictionary to List:", dict_to_list(sample_dict))

