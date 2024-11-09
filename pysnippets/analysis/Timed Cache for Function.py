from functools import lru_cache
import time

@lru_cache(maxsize=None)
def cached_func(x):
    time.sleep(2)  # Simulate a slow function
    return x * x

print(cached_func(2))
