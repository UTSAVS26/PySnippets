from dataclasses import dataclass
import logging

@dataclass
class CoinChangeInput:
    coins: list
    amount: int

def coin_change(input_data: CoinChangeInput):
    coins, amount = input_data.coins, input_data.amount
    try:
        if not coins or amount < 0:
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coin_used = [-1] * (amount + 1)

        for coin in coins:
            for x in range(coin, amount + 1):
                if dp[x - coin] + 1 < dp[x]:
                    dp[x] = dp[x - coin] + 1
                    coin_used[x] = coin

        if dp[amount] == float('inf'):
            return -1

        result_coins = []
        while amount > 0:
            if coin_used[amount] == -1:
                break
            result_coins.append(coin_used[amount])
            amount -= coin_used[amount]

        return len(result_coins), result_coins
    except Exception as e:
        logging.error(f"Error in coin_change function: {e}")
        return None

# Test cases
def test_coin_change():
    test_cases = [
        (CoinChangeInput([1, 2, 5], 11), (3, [5, 5, 1])),
        (CoinChangeInput([2], 3), -1),
        (CoinChangeInput([1], 0), (0, [])),
    ]
    
    for input_data, expected in test_cases:
        result = coin_change(input_data)
        assert result == expected, f"Expected {expected}, got {result}"

if __name__ == "__main__":
    test_coin_change()