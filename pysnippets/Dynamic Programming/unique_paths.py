def unique_paths(m, n):
    # Input validation
    if not (isinstance(m, int) and isinstance(n, int)) or m <= 0 or n <= 0:
        raise ValueError("Both m and n must be positive integers.")

    dp = [1] * n  # Only one row needed for storage, initialized with 1

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]  # Update dp[j] with paths from the cell above

    return dp[-1]  # The last element contains the number of unique paths

if __name__ == "__main__":
    m, n = 3, 7
    num_paths = unique_paths(m, n)  # Output: 28
    print(f"The number of unique paths in a grid of size {m} x {n} is: {num_paths}")