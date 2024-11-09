def unique_paths(m, n):
    # Input validation
    if not (isinstance(m, int) and isinstance(n, int)) or m <= 0 or n <= 0:
        raise ValueError("Both m and n must be positive integers.")

    dp = [1] * n  # Only one row needed for storage, initialized with 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # Update dp[j] with paths from the cell above

    return dp[-1]  # The last element contains the number of unique paths

# Example function definition for testing
def test_unique_paths():
    test_cases = [
        (3, 7, 28),  # Example test case
        (3, 2, 3),
        (7, 3, 28)
    ]
    
    for m, n, expected in test_cases:
        result = unique_paths(m, n)
        assert result == expected, f"Expected {expected}, got {result}"

# Test cases
if __name__ == "__main__":
    test_cases = [
        (3, 7),  # Output: 28
        (3, 2),  # Output: 3
        (1, 1),  # Output: 1
        (5, 5),  # Output: 70
        (2, 3),  # Output: 3
        (7, 3),  # Output: 28
        (10, 10) # Output: 48620
    ]
    
    for m, n in test_cases:
        num_paths = unique_paths(m, n)
        print(f"The number of unique paths in a grid of size {m} x {n} is: {num_paths}")