from typing import Callable


def retry(retries: int = 3) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):  # Allow retries minus one final attempt
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
            # One last attempt without catching an exception
            return func(*args, **kwargs)

        return wrapper

    return decorator
