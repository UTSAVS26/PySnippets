def coin_change(coins, amount):
    # Input validation
    if not coins or amount < 0:
        return -1

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)  # To track coins used

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:  # If using the coin results in fewer coins
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin  # Track the coin used

    if dp[amount] == float('inf'):
        return -1

    # To find the coins used for the minimum coins
    result_coins = []
    while amount > 0:
        if coin_used[amount] == -1:  # No coins could form this amount
            break
        result_coins.append(coin_used[amount])
        amount -= coin_used[amount]

    return dp[amount], result_coins

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11),  # Output: (3, [5, 5, 1])
        ([2], 3),         # Output: -1
        ([1], 0),         # Output: (0, [])
        ([1, 2, 3], 4),   # Output: (2, [1, 1, 2] or [2, 2])
        ([1, 5, 10, 25], 30)  # Output: (2, [25, 5])
    ]
    
    for coins, amount in test_cases:
        min_coins, used_coins = coin_change(coins, amount)
        print(f"Coins: {coins}, Amount: {amount} => Minimum coins needed: {min_coins}, Coins used: {used_coins}")