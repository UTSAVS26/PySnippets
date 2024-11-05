Dictionary Manipulation Module
===============================

Introduction
------------

The **Dictionary Manipulation Module** provides essential functions for working with dictionaries, enabling efficient data handling and analysis. Each function is designed to facilitate common tasks related to dictionary operations.

Functionality
-------------

### Add Item

This function adds a new key-value pair to the dictionary.

    add_item(d, key, value)

- **Args**:
  - `d` (dict): The dictionary to which the item will be added.
  - `key`: The key to add.
  - `value`: The value associated with the key.
- **Returns**:
  - `dict`: The updated dictionary.

**Example**:

    >>> add_item({'a': 1}, 'b', 2)
    {'a': 1, 'b': 2}

---

### Update Item

This function updates the value for an existing key.

    update_item(d, key, value)

- **Args**:
  - `d` (dict): The dictionary to update.
  - `key`: The key whose value will be updated.
  - `value`: The new value to set.
- **Returns**:
  - `dict`: The updated dictionary.

**Example**:

    >>> update_item({'a': 1}, 'a', 2)
    {'a': 2}

---

### Remove Item

This function removes a key-value pair from the dictionary.

    remove_item(d, key)

- **Args**:
  - `d` (dict): The dictionary from which the item will be removed.
  - `key`: The key to remove.
- **Returns**:
  - `dict`: The updated dictionary.

**Example**:

    >>> remove_item({'a': 1, 'b': 2}, 'a')
    {'b': 2}

---

### Check for Key

This function verifies if a specific key exists in the dictionary.

    check_for_key(d, key)

- **Args**:
  - `d` (dict): The dictionary to check.
  - `key`: The key to verify.
- **Returns**:
  - `bool`: `True` if the key exists, `False` otherwise.

**Example**:

    >>> check_for_key({'a': 1}, 'a')
    True

---

### Iterate Keys

This function loops through all the keys in the dictionary.

    iterate_keys(d)

- **Args**:
  - `d` (dict): The dictionary to iterate.
- **Returns**:
  - `list`: A list of keys in the dictionary.

**Example**:

    >>> iterate_keys({'a': 1, 'b': 2})
    ['a', 'b']

---

### Iterate Values

This function loops through all the values in the dictionary.

    iterate_values(d)

- **Args**:
  - `d` (dict): The dictionary to iterate.
- **Returns**:
  - `list`: A list of values in the dictionary.

**Example**:

    >>> iterate_values({'a': 1, 'b': 2})
    [1, 2]

---

### Merge Dictionaries

This function combines two dictionaries into one.

    merge_dictionaries(d1, d2)

- **Args**:
  - `d1` (dict): The first dictionary.
  - `d2` (dict): The second dictionary to merge.
- **Returns**:
  - `dict`: The merged dictionary.

**Example**:

    >>> merge_dictionaries({'a': 1}, {'b': 2})
    {'a': 1, 'b': 2}

---

### Copy Dictionary

This function creates a shallow copy of the dictionary.

    copy_dictionary(d)

- **Args**:
  - `d` (dict): The dictionary to copy.
- **Returns**:
  - `dict`: A shallow copy of the dictionary.

**Example**:

    >>> copy_dictionary({'a': 1})
    {'a': 1}

---

### Clear Dictionary

This function removes all items from the dictionary.

    clear_dictionary(d)

- **Args**:
  - `d` (dict): The dictionary to clear.
- **Returns**:
  - `dict`: An empty dictionary.

**Example**:

    >>> clear_dictionary({'a': 1})
    {}

---

### Find Key by Value

This function retrieves keys that match a specific value.

    find_key_by_value(d, value)

- **Args**:
  - `d` (dict): The dictionary to search.
  - `value`: The value to find.
- **Returns**:
  - `list`: A list of keys that have the specified value.

**Example**:

    >>> find_key_by_value({'a': 1, 'b': 2, 'c': 1}, 1)
    ['a', 'c']

---

### Invert Dictionary

This function swaps keys and values in the dictionary.

    invert_dictionary(d)

- **Args**:
  - `d` (dict): The dictionary to invert.
- **Returns**:
  - `dict`: The inverted dictionary.

**Example**:

    >>> invert_dictionary({'a': 1, 'b': 2})
    {1: 'a', 2: 'b'}

---

### Count Values

This function counts occurrences of each unique value in the dictionary.

    count_values(d)

- **Args**:
  - `d` (dict): The dictionary to analyze.
- **Returns**:
  - `dict`: A dictionary with values as keys and their counts as values.

**Example**:

    >>> count_values({'a': 1, 'b': 2, 'c': 1})
    {1: 2, 2: 1}

---

### Filter by Value

This function filters dictionary items based on a condition function.

    filter_by_value(d, condition)

- **Args**:
  - `d` (dict): The dictionary to filter.
  - `condition`: A function that takes a value and returns `True` if it should be included.
- **Returns**:
  - `dict`: A dictionary containing items that meet the condition.

**Example**:

    >>> filter_by_value({'a': 1, 'b': 2, 'c': 3}, lambda x: x > 1)
    {'b': 2, 'c': 3}

---

### Min and Max Value Keys

This function identifies the keys with the lowest and highest values.

    min_max_value_keys(d)

- **Args**:
  - `d` (dict): The dictionary to analyze.
- **Returns**:
  - `tuple`: A tuple containing the key with the minimum value and the key with the maximum value.

**Example**:

    >>> min_max_value_keys({'a': 1, 'b': 2, 'c': 3})
    ('a', 'c')

---

### Sort by Value

This function sorts dictionary entries by their values.

    sort_by_value(d, reverse=False)

- **Args**:
  - `d` (dict): The dictionary to sort.
  - `reverse` (bool, optional): If `True`, sorts in descending order. Default is `False`.
- **Returns**:
  - `dict`: A sorted dictionary based on values.

**Example**:

    >>> sort_by_value({'a': 3, 'b': 1, 'c': 2})
    {'b': 1, 'c': 2, 'a': 3}

---

### Convert to JSON

This function converts the dictionary to a JSON string.

    to_json(d)

- **Args**:
  - `d` (dict): The dictionary to convert.
- **Returns**:
  - `str`: JSON representation of the dictionary.

**Example**:

    >>> to_json({'a': 1, 'b': 2})
    '{"a": 1, "b": 2}'

---

### Sum Numeric Values

This function sums all numeric values in the dictionary.

    sum_numeric_values(d)

- **Args**:
  - `d` (dict): The dictionary to analyze.
- **Returns**:
  - `float`: Sum of all numeric values.

**Example**:

    >>> sum_numeric_values({'a': 1, 'b': 2, 'c': 'x'})
    3

Feel free to reach out if you have any questions about how to use the Dictionary Manipulation Module!

