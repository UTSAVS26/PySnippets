def lcs(x, y, m, n, memo={}):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        memo[(m, n)] = 1 + lcs(x, y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs(x, y, m, n - 1, memo), lcs(x, y, m - 1, n, memo))
    return memo[(m, n)]

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    print(lcs(x, y, len(x), len(y)))  # Output: 4
