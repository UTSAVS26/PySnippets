def prime_factorization(n: int) -> list:
    """
    Returns the prime factors of the given integer n.

    Args:
        n (int): The integer to factorize. Must be a positive integer.

    Returns:
        list: A list of prime factors of n.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors


if __name__ == "__main__":
    # Example usage
    result = prime_factorization(28)
    print(result)  # Output: [2, 2, 7]
