def longest_common_subsequence(x, y):
    # Input validation
    if not isinstance(x, str) or not isinstance(y, str):
        raise ValueError("Both inputs must be strings.")

    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the LCS
    lcs = []
    while m > 0 and n > 0:
        if x[m - 1] == y[n - 1]:
            lcs.append(x[m - 1])
            m -= 1
            n -= 1
        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    lcs.reverse()  # Reverse the list to get the correct order
    return dp[len(x)][len(y)], ''.join(lcs)

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("AGGTAB", "GXTXAYB"),  # Output: (4, "GTAB")
        ("ABCBDAB", "BDCAB"),   # Output: (4, "BCAB")
        ("", ""),                # Output: (0, "")
        ("ABC", "AC"),          # Output: (2, "AC")
        ("", "A"),              # Output: (0, "")
        ("ABCDEF", "AEBDF"),    # Output: (4, "ABDF")
        ("AGGTAB", "GXTXAYB")   # Output: (4, "GTAB")
    ]
    
    for x, y in test_cases:
        length, sequence = longest_common_subsequence(x, y)
        print(f"The length of the longest common subsequence between '{x}' and '{y}' is: {length}, Sequence: '{sequence}'")