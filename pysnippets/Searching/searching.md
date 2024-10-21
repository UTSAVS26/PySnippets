# Searching Algorithms - PySnippets

Welcome to the **Searching Algorithms Module**! This module provides implementations of various searching algorithms to efficiently find elements in lists. It includes both linear search and binary search methods.

## Table of Contents

- [Introduction](#introduction)
- [Functionality](#functionality)
  - [Linear Search](#linear-search)
  - [Binary Search (Iterative)](#binary-search-iterative)
  - [Binary Search (Recursive)](#binary-search-recursive)
- [Usage Examples](#usage-examples)

---

## Introduction

The **Searching Algorithms Module** offers different methods for searching elements within a list. Each algorithm is designed to demonstrate varying efficiency, providing options for both simple and complex searching needs.

---

## Functionality

### Linear Search

This function implements a linear search algorithm to find the index of an element in a list.

```python
search(arr, N, x)
```

- **Args**:
  - `arr` (list): A list of elements to search through.
  - `N` (int): The number of elements in the list.
  - `x`: The element to search for.
  
- **Returns**:
  - `int`: The index of the element if found, otherwise -1.
  
- **Example**:
  ```python
  >>> linear_search([2, 3, 4, 10, 40], 5, 10)
  3
  ```

---

### Binary Search (Iterative)

This function implements the iterative version of the binary search algorithm.

```python
binarySearchiterative(arr, low, high, x)
```

- **Args**:
  - `arr` (list): A sorted list of elements to search through.
  - `low` (int): The starting index of the list.
  - `high` (int): The ending index of the list.
  - `x`: The element to search for.
  
- **Returns**:
  - `int`: The index of the element if found, otherwise -1.
  
- **Example**:
  ```python
  >>> binarySearchiterative([2, 3, 4, 10, 40], 0, len(arr)-1, 10)
  3
  ```

---

### Binary Search (Recursive)

This function implements the recursive version of the binary search algorithm.

```python
binarySearchrecursive(arr, low, high, x)
```

- **Args**:
  - `arr` (list): A sorted list of elements to search through.
  - `low` (int): The starting index of the list.
  - `high` (int): The ending index of the list.
  - `x`: The element to search for.
  
- **Returns**:
  - `int`: The index of the element if found, otherwise -1.
  
- **Example**:
  ```python
  >>> binarySearchrecursive([2, 3, 4, 10, 40], 0, len(arr)-1, 10)
  3
  ```

