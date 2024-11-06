# Searching Algorithms - PySnippets

Welcome to the **Searching Algorithms Module**! This module provides implementations of various searching algorithms to efficiently find elements in lists. It includes both linear search and binary search methods, among others, all enhanced with type hints, improved docstrings, and logging for better traceability.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Linear Search](#linear-search)
  - [Binary Search (Iterative)](#binary-search-iterative)
  - [Binary Search (Recursive)](#binary-search-recursive)
  - [Exponential Search](#exponential-search)
  - [Fibonacci Search](#fibonacci-search)
  - [Interpolation Search](#interpolation-search)
  - [Jump Search](#jump-search)
  - [Ternary Search](#ternary-search)
- [Usage Examples](#usage-examples)

---

## Introduction

The **Searching Algorithms Module** offers different methods for searching elements within a list. Each algorithm is designed to demonstrate varying efficiency, providing options for both simple and complex searching needs. Enhanced with type hints, logging, and comprehensive docstrings, this module is both user-friendly and developer-friendly.

---

## Functionality

### Linear Search

This function implements a linear search algorithm to find the index of an element in a list.

```python
linear_search(arr: List[int], target: int) -> int
```

- **Args**:
  - `arr` (List[int]): A list of elements to search through.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, otherwise -1.

- **Example**:
  ```python
  >>> linear_search([2, 3, 4, 10, 40], 10)
  3
  ```

---

### Binary Search (Iterative)

This function implements the iterative version of the binary search algorithm.

```python
binary_search_iterative(arr: List[int], low: int, high: int, target: int) -> int
```

- **Args**:
  - `arr` (List[int]): A sorted list of elements to search through.
  - `low` (int): The starting index of the list.
  - `high` (int): The ending index of the list.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, otherwise -1.

- **Example**:
  ```python
  >>> binary_search_iterative([2, 3, 4, 10, 40], 0, len(arr)-1, 10)
  3
  ```

---

### Binary Search (Recursive)

This function implements the recursive version of the binary search algorithm.

```python
binary_search_recursive(arr: List[int], low: int, high: int, target: int) -> int
```

- **Args**:
  - `arr` (List[int]): A sorted list of elements to search through.
  - `low` (int): The starting index of the list.
  - `high` (int): The ending index of the list.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, otherwise -1.

- **Example**:
  ```python
  >>> binary_search_recursive([2, 3, 4, 10, 40], 0, len(arr)-1, 10)
  3
  ```

---

### Exponential Search

This function implements the exponential search algorithm.

```python
exponential_search(arr: List[int], target: int) -> int
```

- **Args**:
  - `arr` (List[int]): Sorted list of elements to search through.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, else -1.

- **Example**:
  ```python
  >>> exponential_search([2, 3, 4, 10, 40], 10)
  3
  ```

---

### Fibonacci Search

This function implements the Fibonacci search algorithm.

```python
fibonacci_search(arr: List[int], target: int) -> int
```

- **Args**:
  - `arr` (List[int]): Sorted list of elements to search through.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, else -1.

- **Example**:
  ```python
  >>> fibonacci_search([2, 3, 4, 10, 40], 10)
  3
  ```

---

### Interpolation Search

This function implements the interpolation search algorithm.

```python
interpolation_search(arr: List[int], target: int) -> int
```

- **Args**:
  - `arr` (List[int]): Sorted list of elements to search through (with uniformly distributed values).
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, else -1.

- **Example**:
  ```python
  >>> interpolation_search([2, 3, 4, 10, 40], 10)
  3
  ```

---

### Jump Search

This function implements the jump search algorithm.

```python
jump_search(arr: List[int], target: int) -> int
```

- **Args**:
  - `arr` (List[int]): Sorted list of elements to search through.
  - `target` (int): The element to search for.

- **Returns**:
  - `int`: The index of the element if found, else -1.

- **Example**:
  ```python
  >>> jump_search([2, 3, 4, 10, 40], 10)
  3
  ```

---

### Ternary Search

This function implements the ternary search algorithm.

```python
ternary_search(arr: List[int], target: int, left: int = 0, right: int = None) -> int
```

- **Args**:
  - `arr` (List[int]): Sorted list of elements to search through.
  - `target` (int): The element to search for.
  - `left` (int, optional): Left boundary for the search. Defaults to 0.
  - `right` (int, optional): Right boundary for the search. Defaults to None.

- **Returns**:
  - `int`: The index of the element if found, else -1.

- **Example**:
  ```python
  >>> ternary_search([2, 3, 4, 10, 40], 10)
  3
  ```

