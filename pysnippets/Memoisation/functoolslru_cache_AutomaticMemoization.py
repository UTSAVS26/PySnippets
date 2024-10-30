
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Returns the nth Fibonacci number using automatic memoization with lru_cache.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
