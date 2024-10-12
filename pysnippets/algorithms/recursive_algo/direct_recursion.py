def direct_recursion(n):
    if n <= 0:
        return 0
    else:
        return n + direct_recursion(n - 1)  # Direct call to itself

# Example usage
print("Direct Recursion Result:", direct_recursion(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)
