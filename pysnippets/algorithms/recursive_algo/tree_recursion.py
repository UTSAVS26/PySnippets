def tree_recursion(n):
    if n <= 1:
        return n
    else:
        return tree_recursion(n - 1) + tree_recursion(n - 2)  # Multiple recursive calls

# Example usage
print("Tree Recursion Result for Fibonacci(5):", tree_recursion(5))  # Output: 5 (0 + 1 + 1 + 2 + 3)
