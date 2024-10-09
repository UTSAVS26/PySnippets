# Utilities - PySnippets

Welcome to the **Utilities** module! This module provides a set of handy, reusable utility functions that can simplify common tasks in Python. Whether you're retrying failed operations, measuring function execution time, or flattening nested lists, these utilities help make your code more efficient and readable.

## Table of Contents

- [Utilities - PySnippets](#utilities---pysnippets)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Functionality](#functionality)
    - [Retry Function](#retry-function)
      - [Function Signature:](#function-signature)
    - [Time Execution](#time-execution)
      - [Function Signature:](#function-signature-1)
    - [Flatten Nested List](#flatten-nested-list)
      - [Function Signature:](#function-signature-2)
  - [Usage Examples](#usage-examples)
    - [Retry Example](#retry-example)
    - [Time Execution Example](#time-execution-example)
    - [Flatten Nested List Example](#flatten-nested-list-example)

---

## Introduction

The **Utilities** module includes the following key functionalities:

1. **Retry Function**: Retries a function if it fails, for a specified number of attempts.
2. **Time Execution**: Measures and prints the execution time of a function.
3. **Flatten Nested List**: Flattens a list of nested lists into a single list.

---

## Functionality

### Retry Function

The `retry` function retries a given function if it fails, up to a specified number of attempts. It’s useful for operations that might fail intermittently, such as network calls or database queries.

#### Function Signature:
```python
from typing import Callable

def retry(func: Callable, retries: int = 3) -> Callable:
    def wrapper(*args, **kwargs):
        for _ in range(retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                last_exception = e
        raise last_exception
    return wrapper
```

- **Args**:
  - `func` (Callable): The function to retry.
  - `retries` (int, optional): The number of retries. Defaults to 3.
- **Returns**:
  - `Callable`: A decorated function that will retry on failure.

---

### Time Execution

The `time_execution` function measures the execution time of the decorated function and prints it. This is useful for performance profiling or for tracking the speed of critical sections of your code.

#### Function Signature:
```python
import time
from typing import Callable

def time_execution(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
```

- **Args**:
  - `func` (Callable): The function whose execution time you want to measure.
- **Returns**:
  - `Callable`: A decorated function that prints its execution time.

---

### Flatten Nested List

The `flatten` function flattens a nested list into a single list. It recursively processes sublists and is useful for simplifying complex nested data structures.

#### Function Signature:
```python
from typing import List, Any

def flatten(nested_list: List[Any]) -> List[Any]:
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list
```

- **Args**:
  - `nested_list` (List[Any]): A list that may contain nested lists.
- **Returns**:
  - `List[Any]`: A flattened version of the input list.

---

## Usage Examples

### Retry Example

```python
from retry import retry

@retry(retries=3)
def unreliable_function(x: int) -> int:
    if x < 5:
        raise ValueError("x is too small")
    return x * 2

print(unreliable_function(6))  # Output: 12
```

### Time Execution Example

```python
from time_execution import time_execution

@time_execution
def slow_function(x: int) -> int:
    time.sleep(2)  # Simulate a slow operation
    return x * 2

print(slow_function(5))  # Prints the execution time and result
```

### Flatten Nested List Example

```python
from flatten import flatten

nested = [[1, 2], [3, [4, 5]], 6]
print(flatten(nested))  # Output: [1, 2, 3, 4, 5, 6]
```

---

Feel free to integrate these utilities into your projects and streamline your Python development. If you have any questions or need additional functionality, feel free to reach out!