from functools import lru_cache
from typing import List, Generator

def fibonacci(n: int) -> List[int]:
    """
    Generates the Fibonacci sequence up to the nth term.
    
    Args:
        n (int): The number of terms to generate.
    
    Returns:
        List[int]: A list containing the Fibonacci sequence up to the nth term.
    
    Example:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])

    return fib_seq


def fibonacci_generator(n: int) -> Generator[int, None, None]:
    """
    Generates the Fibonacci sequence up to the nth term using a generator.
    
    Args:
        n (int): The number of terms to generate.
    
    Yields:
        int: The next term in the Fibonacci sequence.
    
    Example:
        >>> list(fibonacci_generator(5))
        [0, 1, 1, 2, 3]
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@lru_cache(maxsize=None)
def fibonacci_lru(n: int) -> int:
    """
    Computes the nth Fibonacci number using memoization with LRU cache.
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    
    Example:
        >>> fibonacci_lru(5)
        5
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_iterative(n: int) -> int:
    """
    Generates the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence.
    
    Returns:
        int: The nth Fibonacci number.
    
    Example:
        >>> fibonacci_iterative(5)
        5
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Example usage
if __name__ == "__main__":
    # Example of generating a Fibonacci sequence as a list
    print(f"Fibonacci sequence (list): {fibonacci(5)}")

    # Example of generating Fibonacci sequence using a generator
    print(f"Fibonacci sequence (generator): {list(fibonacci_generator(5))}")

    # Example of using LRU cache for nth Fibonacci number
    print(f"5th Fibonacci number (LRU Cache): {fibonacci_lru(5)}")

    # Example of generating nth Fibonacci number iteratively
    print(f"5th Fibonacci number (Iterative): {fibonacci_iterative(5)}")