# List to Comma String - PySnippets

Welcome to the **List to Comma String** module! This utility provides functionality to convert a list of strings into a single comma-separated string, making it easier to display and manage list data.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [List to Comma String](#list-to-comma-string)
- [Usage Example](#usage-example)

---

## Introduction

The **List to Comma String** module allows users to convert a list containing string elements into a nicely formatted comma-separated string. This is particularly useful for displaying lists in a user-friendly format, such as in output messages, reports, or UI elements.

---

## Functionality

### List to Comma String

This function takes a list of strings as an input and returns a single string with the list elements joined by commas.

```python
list_to_comma_string(items)
```

- **Args**: 
  - `items` (list of str): A list of strings to convert.
  
- **Returns**: 
  - `str`: A single comma-separated string.
  
- **Example**:
  ```python
  >>> list_to_comma_string(['apple', 'banana', 'cherry'])
  'apple, banana, cherry'
  ```

- **Error Handling**: 
  - Raises a `ValueError` if any element in the list is not a string.
  
---

## Usage Example

To use the list to comma string functionality, simply call the `list_to_comma_string` function with your list of strings:

```python
if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry"]
    result = list_to_comma_string(my_list)
    print(result)  
```

### Expected Output

```
apple, banana, cherry
```

You can replace `my_list` with any list of strings you want to convert. For example:

```python
if __name__ == "__main__":
    my_list = ["dog", "cat", "hamster"]
    result = list_to_comma_string(my_list)
    print(result)  
```

### Expected Output

```
dog, cat, hamster
```
##
Feel free to reach out if you have any questions about how to use the List to Comma String module!
