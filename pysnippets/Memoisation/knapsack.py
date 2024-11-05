from functools import lru_cache

@lru_cache(maxsize=None)
def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)
    else:
        return max(values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1),
                   knapsack(weights, values, capacity, n - 1))

if __name__ == "__main__":
    weights = (1, 2, 3)
    values = (10, 15, 40)
    capacity = 6
    n = len(values)
    print(knapsack(weights, values, capacity, n))  # Output: 55
    # New test cases
    print(knapsack((1, 2, 3, 4), (10, 20, 30, 40), 6, 4))  # Output: 60
