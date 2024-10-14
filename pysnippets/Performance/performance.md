# Overview

This module provides two utility functions: a memoization decorator to cache results of expensive function calls, and a context manager to measure execution time of code blocks.

## Table of Contents

1. [Requirements](#requirements)
2. [Decorator: `memoize`](#decorator-memoize)
   - [Arguments](#arguments)
   - [Returns](#returns)
   - [Example Usage](#example-usage)
3. [Context Manager: `timer`](#context-manager-timer)
   - [Arguments](#arguments-1)
   - [Returns](#returns-1)
   - [Example Usage](#example-usage-1)

## Requirements

To use this module, you need Python's built-in `functools` and `time` libraries. There are no additional libraries required.

## Decorator: `memoize`

```python
@memoize
def function_name(*args, **kwargs):
    ...
```

A decorator that caches the result of the function, avoiding repeated computations. This decorator is useful for expensive function calls, storing results for a given set of arguments.

### Arguments

- **func** (callable): The function to be memoized.

### Returns

- **callable**: A wrapper function that implements memoization.

### Example Usage

```python
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call will compute the result
print(fibonacci(10))
# Subsequent calls with the same argument will return the cached result
print(fibonacci(10))
```

## Context Manager: `timer`

```python
with timer(description):
    ...
```

A context manager that measures the execution time of a code block.

### Arguments

- **description** (str, optional): A description of the operation being timed. Defaults to 'Execution'.

### Returns

- **None**: This context manager does not return any value.

### Example Usage

```python
with timer("Sample operation"):
    # Simulate some time-consuming operation
    time.sleep(2)
```

This will print:

```
Sample operation took 2.00 seconds
```

---
