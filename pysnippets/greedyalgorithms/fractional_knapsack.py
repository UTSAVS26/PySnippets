def fractional_knapsack(W, n, profits, weights):
    # Calculate profit-to-weight ratio and item index in a list of tuples
    items = sorted([(profits[i], weights[i], profits[i] / weights[i]) for i in range(n)], 
                   key=lambda x: x[2], reverse=True)

    max_profit = 0
    for profit, weight, ratio in items:
        if W == 0:
            break
        # Take as much as possible from the current item
        if weight <= W:
            max_profit += profit
            W -= weight
        else:
            max_profit += ratio * W
            W = 0
    return max_profit

def main():
    # Input the number of items and the knapsack capacity
    n = int(input("Enter the number of items: "))
    W = int(input("Enter the total weight of the knapsack: "))

    # Read profits and weights for items
    profits, weights = [], []
    for i in range(n):
        profit = int(input(f"Enter the profit of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        profits.append(profit)
        weights.append(weight)

    # Calculate maximum profit
    max_profit = fractional_knapsack(W, n, profits, weights)
    print("The maximum profit is:", int(max_profit))

if __name__ == "__main__":
    main()
