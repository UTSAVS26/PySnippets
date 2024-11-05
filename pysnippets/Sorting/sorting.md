# Overview

This module provides a function to sort a list of dictionaries by a specified key. 

## Table of Contents

1. [Function: `sort_dict_list`](#function-sort_dict_list)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)
   

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
2.[Function: 'coctail_sort'](#function-cocktail-sort)
   ```Cocktail Sort is an improved version of Bubble Sort. It also goes through the list, but it moves in both directions. First, it sorts from left to right, pushing the largest unsorted item to the end. Then, it reverses and sorts from right to left, pushing the smallest unsorted item to the beginning```
```Cocktail Sort is often better for large or partly sorted lists because it reduces the number of passes needed.```

   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Raises](#raises)
   - [Example Usage](#example-usage)

## Function: `sort_dict_list`

```python
cocktail_sort(dict_list, key, reverse=False)
```

Sorts a list of dictionaries by a specified key.

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