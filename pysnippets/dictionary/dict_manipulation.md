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

*   **Args**:
    *   `d` (dict): The dictionary to which the item will be added.
    *   `key`: The key to add.
    *   `value`: The value associated with the key.
*   **Returns**:
    *   `dict`: The updated dictionary.

**Example**:

    >>> add_item({'a': 1}, 'b', 2)
    {'a': 1, 'b': 2}

* * *

### Update Item

This function updates the value for an existing key.

    update_item(d, key, value)

*   **Args**:
    *   `d` (dict): The dictionary to update.
    *   `key`: The key whose value will be updated.
    *   `value`: The new value to set.
*   **Returns**:
    *   `dict`: The updated dictionary.

**Example**:

    >>> update_item({'a': 1}, 'a', 2)
    {'a': 2}

* * *

### Remove Item

This function removes a key-value pair from the dictionary.

    remove_item(d, key)

*   **Args**:
    *   `d` (dict): The dictionary from which the item will be removed.
    *   `key`: The key to remove.
*   **Returns**:
    *   `dict`: The updated dictionary.

**Example**:

    >>> remove_item({'a': 1, 'b': 2}, 'a')
    {'b': 2}

* * *

### Check for Key

This function verifies if a specific key exists in the dictionary.

    check_for_key(d, key)

*   **Args**:
    *   `d` (dict): The dictionary to check.
    *   `key`: The key to verify.
*   **Returns**:
    *   `bool`: `True` if the key exists, `False` otherwise.

**Example**:

    >>> check_for_key({'a': 1}, 'a')
    True

* * *

### Iterate Keys

This function loops through all the keys in the dictionary.

    iterate_keys(d)

*   **Args**:
    *   `d` (dict): The dictionary to iterate.
*   **Returns**:
    *   `list`: A list of keys in the dictionary.

**Example**:

    >>> iterate_keys({'a': 1, 'b': 2})
    ['a', 'b']

* * *

### Iterate Values

This function loops through all the values in the dictionary.

    iterate_values(d)

*   **Args**:
    *   `d` (dict): The dictionary to iterate.
*   **Returns**:
    *   `list`: A list of values in the dictionary.

**Example**:

    >>> iterate_values({'a': 1, 'b': 2})
    [1, 2]

* * *

### Merge Dictionaries

This function combines two dictionaries into one.

    merge_dictionaries(d1, d2)

*   **Args**:
    *   `d1` (dict): The first dictionary.
    *   `d2` (dict): The second dictionary to merge.
*   **Returns**:
    *   `dict`: The merged dictionary.

**Example**:

    >>> merge_dictionaries({'a': 1}, {'b': 2})
    {'a': 1, 'b': 2}

* * *

### Copy Dictionary

This function creates a shallow copy of the dictionary.

    copy_dictionary(d)

*   **Args**:
    *   `d` (dict): The dictionary to copy.
*   **Returns**:
    *   `dict`: A shallow copy of the dictionary.

**Example**:

    >>> copy_dictionary({'a': 1})
    {'a': 1}

* * *

### Clear Dictionary

This function removes all items from the dictionary.

    clear_dictionary(d)

*   **Args**:
    *   `d` (dict): The dictionary to clear.
*   **Returns**:
    *   `dict`: An empty dictionary.

**Example**:

    >>> clear_dictionary({'a': 1})
    {}

* * *

Feel free to reach out if you have any questions about how to use the Dictionary Manipulation Module!

