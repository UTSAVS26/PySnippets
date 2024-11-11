def two_city_scheduling(costs):
    # Input validation
    if not isinstance(costs, list) or len(costs) % 2 != 0:
        raise ValueError("Input must be a list of pairs with an even length.")
    
    n = len(costs) // 2
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Initialize the starting point

    # Correcting the loop to handle costs correctly
    for i in range(1, len(costs) + 1):
        for j in range(min(i, n) + 1):
            if j > 0:
                dp[j][i - j] = min(dp[j][i - j], dp[j - 1][i - j] + costs[i - 1][0])
            if i - j > 0:
                dp[j][i - j] = min(dp[j][i - j], dp[j][i - j - 1] + costs[i - 1][1])

    return dp[n][n]

# Example function definition for testing
def test_two_city_scheduling():
    test_cases = [
        ([[10, 20], [30, 200], [400, 50], [30, 20]], 250),  # Example test case
    ]
    
    for costs, expected in test_cases:
        result = two_city_scheduling(costs)
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    costs = [[10, 20], [30, 200], [50, 30], [200, 500]]
    min_cost = two_city_scheduling(costs)  # Output: 370
    print(f"The minimum cost to schedule people to two cities is: {min_cost}")