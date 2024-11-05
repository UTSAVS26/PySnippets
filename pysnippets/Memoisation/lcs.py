from functools import lru_cache

@lru_cache(maxsize=None)
def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    else:
        return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))

if __name__ == "__main__":
    x = "AGGTAB"
    y = "GXTXAYB"
    print(lcs(x, y, len(x), len(y)))  # Output: 4
    # New test cases
    print(lcs("ABC", "AC", len("ABC"), len("AC")))  # Output: 2
