def fibonacci_sequence(count=None, max_value=None):
    """
    Generate a Fibonacci sequence up to a specified count or maximum value.
    
    Args:
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.
        
    Returns:
        list: List of Fibonacci numbers.
    """
    if count is None and max_value is None:
        raise ValueError("Either 'count' or 'max_value' must be provided.")
    
    if count is not None and count <= 0:
        raise ValueError("'count' must be a positive integer.")
    
    if max_value is not None and max_value < 0:
        raise ValueError("'max_value' must be a non-negative integer.")
    
    sequence = []
    a, b = 0, 1
    
    while (count is None or len(sequence) < count) and (max_value is None or a <= max_value):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def fibonacci_recursive(n):
    """
    Generate the nth Fibonacci number using recursion.
    
    Args:
        n (int): The nth Fibonacci number to generate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    
fib_cache = {}

def fibonacci_memoized(n):
    """
    Generate the nth Fibonacci number using recursion with memoization.
    
    Args:
        n (int): The nth Fibonacci number to generate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n in fib_cache:
        return fib_cache[n]
    
    if n <= 1:
        fib_cache[n] = n
    else:
        fib_cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    
    return fib_cache[n]

def fibonacci_generator(count=None, max_value=None):
    """
    Generate Fibonacci numbers as a generator.
    
    Args:
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.
        
    Yields:
        int: Next Fibonacci number in sequence.
    """
    a, b = 0, 1
    while (count is None or count > 0) and (max_value is None or a <= max_value):
        yield a
        a, b = b, a + b
        if count is not None:
            count -= 1

def fibonacci_negative(n):
    """
    Generate Fibonacci number for negative indices (Negafibonacci).
    
    Args:
        n (int): Negative Fibonacci index.
        
    Returns:
        int: Fibonacci number for the given negative index.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return (-1) ** (abs(n) + 1) * fibonacci_negative(abs(n))
    else:
        return fibonacci_negative(n - 1) + fibonacci_negative(n - 2)

def fibonacci_custom_start(a, b, count=None, max_value=None):
    """
    Generate Fibonacci sequence with custom starting values.
    
    Args:
        a (int): First number of the custom sequence.
        b (int): Second number of the custom sequence.
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.
        
    Returns:
        list: Fibonacci sequence with custom start values.
    """
    sequence = [a, b]
    while (count is None or len(sequence) < count) and (max_value is None or sequence[-1] <= max_value):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def fibonacci_ratio(n):
    """
    Calculate the ratio of consecutive Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate.
        
    Returns:
        list: List of ratios of consecutive Fibonacci numbers.
    """
    sequence = fibonacci_sequence(count=n)
    ratios = [sequence[i + 1] / sequence[i] for i in range(len(sequence) - 1) if sequence[i] != 0]
    return ratios

def fibonacci_list_or_tuple(count=None, max_value=None, return_type="list"):
    """
    Generate Fibonacci sequence and return it as a list or tuple.
    
    Args:
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.
        return_type (str, optional): 'list' to return a list or 'tuple' to return a tuple. Default is 'list'.
        
    Returns:
        list or tuple: Fibonacci sequence.
    """
    sequence = fibonacci_sequence(count=count, max_value=max_value)
    if return_type == "tuple":
        return tuple(sequence)
    return sequence

def fibonacci_sum(count=None, max_value=None):
    """
    Calculate the sum of the Fibonacci sequence.
    
    Args:
        count (int, optional): Number of Fibonacci numbers to generate.
        max_value (int, optional): Maximum value of Fibonacci numbers.
        
    Returns:
        int: Sum of the Fibonacci sequence.
    """
    sequence = fibonacci_sequence(count=count, max_value=max_value)
    return sum(sequence)

def fibonacci_module(n, mod):
    """
    Generate Fibonacci sequence and return the numbers modulo a given number.
    
    Args:
        n (int): Number of Fibonacci numbers to generate.
        mod (int): Modulo value.
        
    Returns:
        list: List of Fibonacci numbers modulo the given value.
    """
    sequence = fibonacci_sequence(count=n)
    return [num % mod for num in sequence]

def nth_fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Args:
        n (int): The nth Fibonacci number to generate.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    
    print(fibonacci_sequence(count=10))
    print(fibonacci_recursive(10))
    print(fibonacci_memoized(10))
    
    for fib in fibonacci_generator(count=10):
        print(fib, end=" ")
        
    print(fibonacci_custom_start(3, 5, count=5))
    
    print(fibonacci_ratio(10))
    print(fibonacci_list_or_tuple(count=5, return_type="tuple"))
    
    print(fibonacci_sum(count=10))
    print(fibonacci_module(10, 3))
    print(nth_fibonacci(10))
