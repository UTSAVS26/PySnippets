from functools import wraps


def memoize(func):
    """
    A decorator that caches the result of the function, avoiding repeated computations.

    This decorator is useful for expensive function calls. It will store the results of the function
    for a given set of arguments and return the cached results when the function is called again with
    the same arguments.

    Args:
        func (callable): The function to be memoized.

    Returns:
        callable: A wrapper function that implements memoization.

    Example:
        @memoize
        def fibonacci(n):
            if n < 2:
                return n:
            return fibonacci(n-1) + fibonacci(n-2)

        # first call will compute the result
        print(fibonacci(10))
        # subsequent calls with the same argument will return the cached result
        print(fibonacci(10))
    """
    cache = {}

    @wraps(func)  # copies/retains the metadata from the original function
    def wrapper(*args, **kwargs):
        # create a key that uniquely identifies the function call
        key = str(args) + str(kwargs)

        # if this function call is not cached, compute and cache the result
        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


# example usage
if __name__ == "__main__":

    @memoize
    def expensive_function(x, y):
        import time

        time.sleep(2)  # simulate an expensive operation
        return x + y

    # first call will take about 2 seconds
    print(expensive_function(2, 3))

    # second call with the same arguments will be instant
    print(expensive_function(2, 3))
