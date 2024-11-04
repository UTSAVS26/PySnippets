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

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    length, sequence = longest_common_subsequence(x, y)  # Output: (4, "GTAB")
    print(f"The length of the longest common subsequence is: {length}")
    print(f"The longest common subsequence is: '{sequence}'")