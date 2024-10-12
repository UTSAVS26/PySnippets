def head_recursion(n):
    if n <= 0:
        return 0
    else:
        head_recursion(n - 1)  # Head call
        return n  # Executes after returning from the recursive calls

# Example usage
result = 0
for i in range(1, 6):
    result += head_recursion(i)  # Sum the values from head recursion
print("Head Recursion Result:", result)  # Output: 15 (5 + 4 + 3 + 2 + 1)
