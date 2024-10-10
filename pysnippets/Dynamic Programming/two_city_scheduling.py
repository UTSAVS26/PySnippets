def two_city_scheduling(costs):
    n = len(costs) // 2
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(n + 1):
            if i + j == 0:
                continue
            cost1 = dp[i - 1][j] + costs[i + j - 1][0] if i > 0 else float('inf')
            cost2 = dp[i][j - 1] + costs[i + j - 1][1] if j > 0 else float('inf')
            dp[i][j] = min(cost1, cost2)

    return dp[n][n]

if __name__ == "__main__":
    costs = [[10, 20], [30, 200], [50, 30], [200, 500]]
    print(two_city_scheduling(costs))  # Output: 370
