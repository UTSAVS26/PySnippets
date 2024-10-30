
# Using functools.lru_cache for Automatic Memoization

## Overview

This project demonstrates the use of `functools.lru_cache` to implement automatic memoization in Python, specifically for calculating Fibonacci numbers. This approach helps in optimizing recursive functions by caching previous results.

## Files

- **dictionarywithlru.py**: Contains the `fibonacci` function with `@lru_cache` decorator to enable memoization.
- **test_dictionarywithlru.py**: Contains unit tests for `fibonacci`, verifying the efficiency and accuracy of the memoized function.

## Example

The `fibonacci` function calculates the nth Fibonacci number efficiently due to memoization, with cached results avoiding redundant calculations.

## How to Run Tests

To run the unit tests, execute:

```bash
python -m unittest test_dictionarywithlru.py
```

This will validate that the function works correctly with memoization enabled.
