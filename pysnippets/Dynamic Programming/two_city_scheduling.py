def two_city_scheduling(costs):
    # Input validation
    if not isinstance(costs, list) or len(costs) % 2 != 0:
        raise ValueError("Input must be a list of pairs with an even length.")
    
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
    min_cost = two_city_scheduling(costs)  # Output: 370
    print(f"The minimum cost to schedule people to two cities is: {min_cost}")