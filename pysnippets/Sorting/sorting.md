# Overview

This module provides multiple functions to sort a list of dictionaries by a specified key using various sorting algorithms. The sorting algorithms implemented include Cocktail Sort, Heap Sort, and Counting Sort. Each function is designed to efficiently sort a list of dictionaries based on a specific key, with options for ascending or descending order.

## Table of Contents

1. [Function: `sort_dict_list`](#function-sort_dict_list)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)
   - [Approach](#approach)
   - [Usage Instructions](#usage-instructions)

2. [Function: `cocktail_sort`](#function-cocktail_sort)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)
   - [Approach](#approach)
   - [Usage Instructions](#usage-instructions)

3. [Function: `heap_sort`](#function-heap_sort)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)
   - [Approach](#approach)
   - [Usage Instructions](#usage-instructions)

4. [Function: `counting_sort`](#function-counting_sort)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)
   - [Approach](#approach)
   - [Usage Instructions](#usage-instructions)

## Function: `sort_dict_list`

```python
sort_dict_list(dict_list, key, reverse=False)
```

Sorts a list of dictionaries by a specified key using the cocktail sort algorithm, with the option to sort in ascending or descending order.

### Arguments

- **dict_list** (list): A list of dictionaries to be sorted.
- **key** (str): The dictionary key to sort by.
- **reverse** (bool, optional): If `True`, sort in descending order. Default is `False` (ascending order).

### Returns

- **list**: A new list of dictionaries sorted by the specified key.

### Raises

- **ValueError**: If the list is empty or if the specified key is not present in all dictionaries.
- **ValueError**: If an unsupported sorting method is specified.

### Example Usage

```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

sorted_data = sort_dict_list(data, key="age")
print(sorted_data)

# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### Approach

The `sort_dict_list` function iterates through the list of dictionaries, comparing adjacent elements based on the specified key. It swaps elements if they are in the wrong order, repeating this process until the list is sorted. This approach utilizes the cocktail sort algorithm, which is a variation of the bubble sort algorithm that sorts in both directions, improving efficiency for larger or partly sorted lists.

### Usage Instructions

To use the `sort_dict_list` function, ensure that the list of dictionaries is not empty and that all dictionaries contain the specified key. The function returns a new sorted list of dictionaries, leaving the original list unchanged. You can specify the sorting order by setting the `reverse` argument to `True` for descending order or `False` for ascending order (default). Additionally, you can choose the sorting algorithm by specifying the `method` argument (e.g., 'quick', 'merge').

---

## Function: `cocktail_sort`

```python
cocktail_sort(dict_list, key, reverse=False)
```

Sorts a list of dictionaries by a specified key using the cocktail sort algorithm, with the option to sort in ascending or descending order.

### Arguments

- **dict_list** (list): A list of dictionaries to be sorted.
- **key** (str): The dictionary key to sort by.
- **reverse** (bool, optional): If `True`, sort in descending order. Default is `False` (ascending order).

### Returns

- **list**: A new list of dictionaries sorted by the specified key.

### Raises

- **ValueError**: If the list is empty or if the specified key is not present in all dictionaries.

### Example Usage

```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

sorted_data = cocktail_sort(data, key="age")
print(sorted_data)

# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### Approach

The `cocktail_sort` function iterates through the list of dictionaries, comparing adjacent elements based on the specified key. It swaps elements if they are in the wrong order, repeating this process until the list is sorted. This approach is known as the cocktail sort algorithm, which is a variation of the bubble sort algorithm that sorts in both directions. The cocktail sort algorithm is more efficient than the bubble sort algorithm for large or partly sorted lists as it reduces the number of passes needed to sort the list.

### Usage Instructions

To use the `cocktail_sort` function, ensure that the list of dictionaries is not empty and that all dictionaries contain the specified key. The function returns a new sorted list of dictionaries, leaving the original list unchanged. You can specify the sorting order by setting the `reverse` argument to `True` for descending order or `False` for ascending order (default). The `cocktail_sort` function is particularly useful for large or partly sorted lists, as it reduces the number of passes needed to sort the list.

---

## Function: `heap_sort`

```python
heap_sort(dict_list, key, reverse=False)
```

Sorts a list of dictionaries using the Heap Sort algorithm based on a specified key, with the option to sort in ascending or descending order.

### Arguments

- **dict_list** (list): A list of dictionaries to be sorted.
- **key** (str): The dictionary key to sort by.
- **reverse** (bool, optional): If `True`, sort in descending order. Default is `False` (ascending order).

### Returns

- **list**: A new list of dictionaries sorted by the specified key.

### Raises

- **ValueError**: If the list is empty or if the specified key is not present in all dictionaries.
- **ValueError**: If an unsupported sorting method is specified.

### Example Usage

```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

sorted_data = heap_sort(data, key="age")
print(sorted_data)

# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### Approach

The `heap_sort` function builds a heap from the list of dictionaries based on the specified key and then extracts elements from the heap to sort the list. This approach ensures that the list is sorted in-place with optimal time complexity for heap-based sorting.

### Usage Instructions

To use the `heap_sort` function, ensure that the list of dictionaries is not empty and that all dictionaries contain the specified key. The function returns a new sorted list of dictionaries, leaving the original list unchanged. You can specify the sorting order by setting the `reverse` argument to `True` for descending order or `False` for ascending order (default).

---

## Function: `counting_sort`

```python
counting_sort(dict_list, key, reverse=False)
```

Sorts a list of dictionaries using the Counting Sort algorithm based on a specified key, with the option to sort in ascending or descending order.

### Arguments

- **dict_list** (list): A list of dictionaries to be sorted.
- **key** (str): The dictionary key to sort by.
- **reverse** (bool, optional): If `True`, sort in descending order. Default is `False` (ascending order).

### Returns

- **list**: A new list of dictionaries sorted by the specified key.

### Raises

- **ValueError**: If the list is empty or if the specified key is not present in all dictionaries.
- **ValueError**: If an unsupported sorting method is specified.
- **ValueError**: If the key values are not non-negative integers.

### Example Usage

```python
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

sorted_data = counting_sort(data, key="age")
print(sorted_data)

# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
```

### Approach

The `counting_sort` function sorts the list by counting the occurrences of each key value and calculating the positions of each element in the sorted list. This non-comparative sorting algorithm is efficient for datasets with a limited range of key values.

### Usage Instructions

To use the `counting_sort` function, ensure that:

- The list of dictionaries is not empty.
- All dictionaries contain the specified key.
- All key values are non-negative integers.

The function returns a new sorted list of dictionaries, leaving the original list unchanged. You can specify the sorting order by setting the `reverse` argument to `True` for descending order or `False` for ascending order (default). Counting Sort is particularly efficient for datasets with a limited range of integer key values.

---

### **4. Update `test_sorting.py` to Include Tests for New Sorting Functions**
