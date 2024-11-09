import functools

def cache(func):
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args not in cached_results:
            cached_results[args] = func(*args)
        return cached_results[args]
    
    return wrapper
