def tail_recursion(n, accumulator=0):
    if n <= 0:
        return accumulator
    else:
        return tail_recursion(n - 1, accumulator + n)  # Tail call with accumulator

# Example usage
print("Tail Recursion Result:", tail_recursion(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)
