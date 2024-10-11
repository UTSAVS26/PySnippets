  List Manipulation Module body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; } h1, h2, h3 { color: #333; } code { background-color: #f4f4f4; padding: 5px; border-radius: 3px; } pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; } hr { margin: 20px 0; }

List Manipulation Module
========================

Introduction
------------

The **List Manipulation Module** provides essential functions for working with lists, enabling efficient data handling and analysis. Each function is designed to facilitate common tasks related to list operations.

Functionality
-------------

### Remove Duplicates

This function removes duplicate elements from the list while maintaining the original order.

    remove_duplicates(lst)

*   **Args**:
    *   `lst` (list): A list from which to remove duplicates.
*   **Returns**:
    *   `list`: A list without duplicates.

**Example**:

    >>> remove_duplicates([1, 2, 2, 3, 4, 4])
    [1, 2, 3, 4]

* * *

### Flatten Nested List

This function flattens a nested list into a single list.

    flatten_nested_list(nested_list)

*   **Args**:
    *   `nested_list` (list): A nested list to flatten.
*   **Returns**:
    *   `list`: A flattened list.

**Example**:

    >>> flatten_nested_list([[1, 2], [3, 4], [5]])
    [1, 2, 3, 4, 5]

* * *

### List Intersection

This function finds the intersection of two lists.

    list_intersection(lst1, lst2)

*   **Args**:
    *   `lst1` (list): The first list.
    *   `lst2` (list): The second list.
*   **Returns**:
    *   `list`: The intersection of the two lists.

**Example**:

    >>> list_intersection([1, 2, 3], [2, 3, 4])
    [2, 3]

* * *

### Random Shuffle

This function randomly shuffles the elements of the list.

    random_shuffle(lst)

*   **Args**:
    *   `lst` (list): A list to shuffle.
*   **Returns**:
    *   `list`: A shuffled list (order will vary).

**Example**:

    >>> random_shuffle([1, 2, 3, 4])
    [3, 1, 4, 2]  # (order will vary)

* * *

### Sort by Frequency

This function sorts the list based on the frequency of elements in descending order.

    sort_by_frequency(lst)

*   **Args**:
    *   `lst` (list): A list to sort by frequency.
*   **Returns**:
    *   `list`: The sorted list by frequency.

**Example**:

    >>> sort_by_frequency([4, 5, 6, 4, 5, 4])
    [4, 4, 4, 5, 5, 6]

* * *

Feel free to reach out if you have any questions about how to use the List Manipulation Module!
