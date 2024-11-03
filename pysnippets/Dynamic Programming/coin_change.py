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

if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    min_coins, used_coins = coin_change(coins, amount)  # Output: (3, [5, 5, 1])
    if min_coins != -1:
        print(f"Minimum coins needed: {min_coins}")
        print(f"Coins used: {used_coins}")
    else:
        print("Amount cannot be formed with the given coins.")