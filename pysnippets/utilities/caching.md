
# Caching Function Results

This snippet uses a decorator to cache results of expensive function calls, which can significantly improve performance.

## Code
```python
import functools

def cache(func):
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    
    return wrapper
```

## Usage
```python
@cache
def expensive_function(n):
    print(f"Calculating {n}...")
    return n * n

print(expensive_function(4))
print(expensive_function(4))  # This will use the cached result
```
