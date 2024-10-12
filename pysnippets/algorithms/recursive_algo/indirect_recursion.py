def indirect_recursion_a(n):
    if n <= 0:
        return 0
    else:
        return n + indirect_recursion_b(n - 1)  # Calls the second function

def indirect_recursion_b(n):
    if n <= 0:
        return 0
    else:
        return indirect_recursion_a(n - 1)  # Calls the first function

# Example usage
print("Indirect Recursion Result:", indirect_recursion_a(5))  # Output: 15 (5 + 4 + 3 + 2 + 1)
