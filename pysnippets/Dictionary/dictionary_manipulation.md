  Dictionary Manipulation Module Documentation body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; padding: 20px; background-color: #f4f4f4; border-radius: 8px; } h1, h2, h3 { color: #333; } code { background: #eaeaea; padding: 2px 5px; border-radius: 4px; } pre { background: #eaeaea; padding: 10px; border-radius: 4px; }

Dictionary Manipulation Module
==============================

Welcome to the **Dictionary Manipulation Module**! This module provides a collection of functions for manipulating dictionaries in Python.

Functions Overview
------------------

*   [merge\_dicts](#merge_dicts)
*   [filter\_dict\_by\_value](#filter_dict_by_value)
*   [get\_keys\_with\_value](#get_keys_with_value)
*   [invert\_dict](#invert_dict)
*   [dict\_to\_list](#dict_to_list)

merge\_dicts
------------

Merges two dictionaries into one. If keys are duplicated, values from the second dictionary will overwrite those from the first.

    merge_dicts(dict1, dict2)

*   **Args:**
    *   `dict1` (dict): First dictionary.
    *   `dict2` (dict): Second dictionary.
*   **Returns:** `dict`: The merged dictionary.
*   **Example:**

    merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})  # {'a': 1, 'b': 3, 'c': 4}

filter\_dict\_by\_value
-----------------------

Filters the dictionary, returning only items where the value is above the given threshold.

    filter_dict_by_value(d, threshold)

*   **Args:**
    *   `d` (dict): The dictionary to filter.
    *   `threshold` (int): The threshold value.
*   **Returns:** `dict`: Filtered dictionary.
*   **Example:**

    filter_dict_by_value({'a': 1, 'b': 5, 'c': 3}, 2)  # {'b': 5, 'c': 3}

get\_keys\_with\_value
----------------------

Returns a list of keys that have the specified value.

    get_keys_with_value(d, target_value)

*   **Args:**
    *   `d` (dict): The dictionary to search.
    *   `target_value`: The value to search for.
*   **Returns:** `list`: List of keys with the specified value.
*   **Example:**

    get_keys_with_value({'a': 1, 'b': 2, 'c': 1}, 1)  # ['a', 'c']

invert\_dict
------------

Inverts a dictionary, swapping its keys and values. If there are duplicate values, only one will be kept.

    invert_dict(d)

*   **Args:**
    *   `d` (dict): The dictionary to invert.
*   **Returns:** `dict`: Inverted dictionary.
*   **Example:**

    invert_dict({'a': 1, 'b': 2, 'c': 1})  # {1: 'c', 2: 'b'}

dict\_to\_list
--------------

Converts a dictionary into a list of tuples (key, value).

    dict_to_list(d)

*   **Args:**
    *   `d` (dict): The dictionary to convert.
*   **Returns:** `list`: List of key-value tuples.
*   **Example:**

    dict_to_list({'a': 1, 'b': 2})  # [('a', 1), ('b', 2)]

Conclusion
----------

This Dictionary Manipulation Module provides a set of useful functions for common dictionary operations, enabling efficient data handling in Python.
