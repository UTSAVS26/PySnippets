from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Returns the nth Fibonacci number using automatic memoization with lru_cache.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(10))  # Output: 55
    # New test cases
    print(fibonacci(20))  # Output: 6765
    print(fibonacci(30))  # Output: 832040
