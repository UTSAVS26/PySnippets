def knapsack(weights, values, capacity, n, memo={}):
    if (n, capacity) in memo:
        return memo[(n, capacity)]
    if n == 0 or capacity == 0:
        return 0
    if weights[n - 1] > capacity:
        memo[(n, capacity)] = knapsack(weights, values, capacity, n - 1, memo)
    else:
        memo[(n, capacity)] = max(values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1, memo),
                                   knapsack(weights, values, capacity, n - 1, memo))
    return memo[(n, capacity)]

if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [10, 15, 40]
    capacity = 6
    n = len(values)
    print(knapsack(weights, values, capacity, n))  # Output: 55
