import time
from contextlib import (
    contextmanager,
)  # helps in defining a block of setup and teardown logic


@contextmanager
def timer(description="Execution"):
    """
    A context manager that measures the execution time of a code block.

    Args:
        description (str, optional): A description of the operation being timed. Defaults to 'Execution'.

    Yields:
        None

    Example:
        with timer('Database query'):
            # some time-consuming operation
            time.sleep(2)

    This will print:
    Database query took 2.00 seconds
    """
    start = time.time()
    yield
    elapsed = time.time() - start
    print(f"{description} took {elapsed:.2f} seconds")


# example usage
if __name__ == "__main__":
    with timer("Sample operation"):
        # simulate some time-consuming operation
        time.sleep(2)
