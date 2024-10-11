def fibonacci(n):
    """
    Generates the Fibonacci sequence up to the nth term.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the Fibonacci sequence up to the nth term.

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

# Example usage
if __name__ == "__main__":
    print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
