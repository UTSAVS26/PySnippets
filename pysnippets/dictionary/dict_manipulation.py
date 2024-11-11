import json

def add_item(d: dict, key, value) -> dict:
    """
    Adds a new key-value pair to the dictionary.

    Example usage:
    add_item({'a': 1}, 'b', 2) -> {'a': 1, 'b': 2}
    """
    d[key] = value
    return d

def update_item(d: dict, key, value) -> dict:
    """
    Updates the value for an existing key.

    Example usage:
    update_item({'a': 1}, 'a', 2) -> {'a': 2}
    """
    if key in d:
        d[key] = value
    return d

def remove_item(d: dict, key) -> dict:
    """
    Removes a key-value pair from the dictionary.

    Example usage:
    remove_item({'a': 1, 'b': 2}, 'a') -> {'b': 2}
    """
    d.pop(key, None)
    return d

def check_for_key(d: dict, key) -> bool:
    """
    Verifies if a specific key exists in the dictionary.

    Example usage:
    check_for_key({'a': 1}, 'a') -> True
    """
    return key in d

def iterate_keys(d: dict) -> list:
    """
    Loops through all the keys in the dictionary.

    Example usage:
    iterate_keys({'a': 1, 'b': 2}) -> ['a', 'b']
    """
    return list(d.keys())

def iterate_values(d: dict) -> list:
    """
    Loops through all the values in the dictionary.

    Example usage:
    iterate_values({'a': 1, 'b': 2}) -> [1, 2]
    """
    return list(d.values())

def merge_dictionaries(d1: dict, d2: dict) -> dict:
    """
    Combines two dictionaries into one.

    Example usage:
    merge_dictionaries({'a': 1}, {'b': 2}) -> {'a': 1, 'b': 2}
    """
    d1.update(d2)
    return d1

def copy_dictionary(d: dict) -> dict:
    """
    Creates a shallow copy of the dictionary.

    Example usage:
    copy_dictionary({'a': 1}) -> {'a': 1}
    """
    return d.copy()

def clear_dictionary(d: dict) -> dict:
    """
    Removes all items from the dictionary.

    Example usage:
    clear_dictionary({'a': 1}) -> {}
    """
    d.clear()
    return d

def find_key_by_value(d: dict, value) -> list:
    """
    Retrieves keys that match a specific value.

    Example usage:
    find_key_by_value({'a': 1, 'b': 2, 'c': 1}, 1) -> ['a', 'c']
    """
    return [k for k, v in d.items() if v == value]

def invert_dictionary(d: dict) -> dict:
    """
    Swaps keys and values in the dictionary.

    Example usage:
    invert_dictionary({'a': 1, 'b': 2}) -> {1: 'a', 2: 'b'}
    """
    return {v: k for k, v in d.items()}

def count_values(d: dict) -> dict:
    """
    Counts occurrences of each unique value in the dictionary.

    Example usage:
    count_values({'a': 1, 'b': 2, 'c': 1}) -> {1: 2, 2: 1}
    """
    counts = {}
    for value in d.values():
        counts[value] = counts.get(value, 0) + 1
    return counts

def filter_by_value(d: dict, condition) -> dict:
    """
    Filters dictionary items based on a condition function.

    Example usage:
    filter_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1) -> {'b': 2, 'c': 3}
    """
    return {k: v for k, v in d.items() if condition(v)}

def min_max_value_keys(d: dict) -> tuple:
    """
    Identifies keys with the lowest and highest values in the dictionary.

    Example usage:
    min_max_value_keys({'a': 1, 'b': 2, 'c': 3}) -> ('a', 'c')
    """
    if not d:
        return None, None
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    return min_key, max_key

def sort_by_value(d: dict, reverse=False) -> dict:
    """
    Sorts dictionary entries by their values.

    Example usage:
    sort_by_value({'a': 3, 'b': 1, 'c': 2}) -> {'b': 1, 'c': 2, 'a': 3}
    """
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))

def to_json(d: dict) -> str:
    """
    Converts the dictionary to a JSON string.

    Example usage:
    to_json({'a': 1, 'b': 2}) -> '{"a": 1, "b": 2}'
    """
    return json.dumps(d)

def sum_numeric_values(d: dict) -> float:
    """
    Sums all numeric values in the dictionary.

    Example usage:
    sum_numeric_values({'a': 1, 'b': 2, 'c': 'x'}) -> 3
    """
    return sum(v for v in d.values() if isinstance(v, (int, float)))

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_dict = {'name': 'Alice', 'age': 30, 'salary': 50000, 'department': 'Engineering'}

    print("Original Dictionary:", sample_dict)
    print("After Adding Job:", add_item(sample_dict.copy(), 'job', 'Engineer'))
    print("After Updating Age:", update_item(sample_dict.copy(), 'age', 31))
    print("After Removing Name:", remove_item(sample_dict.copy(), 'name'))
    print("Does Age Exist?:", check_for_key(sample_dict, 'age'))
    print("Iterating Keys:", iterate_keys(sample_dict))
    print("Iterating Values:", iterate_values(sample_dict))
    print("Merging with Another Dictionary:", merge_dictionaries(sample_dict.copy(), {'city': 'New York'}))
    print("Copied Dictionary:", copy_dictionary(sample_dict))
    print("Cleared Dictionary:", clear_dictionary(sample_dict.copy()))

    print("Find Key by Value (50000):", find_key_by_value(sample_dict, 50000))
    print("Inverted Dictionary:", invert_dictionary(sample_dict))
    print("Count Values:", count_values(sample_dict))
    print("Filter by Value (>10000):", filter_by_value(sample_dict, lambda x: isinstance(x, int) and x > 10000))
    print("Min and Max Value Keys:", min_max_value_keys({'a': 1, 'b': 2, 'c': 3}))
    print("Sorted by Value:", sort_by_value({'a': 3, 'b': 1, 'c': 2}))
    print("Dictionary as JSON:", to_json(sample_dict))
    print("Sum of Numeric Values:", sum_numeric_values(sample_dict))

