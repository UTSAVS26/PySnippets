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

# Example usage of the functions in the script
if __name__ == "__main__":
    sample_dict = {'name': 'Alice', 'age': 30}

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

