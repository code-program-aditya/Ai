def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    max_profit = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    selected_items.reverse()  
    return max_profit, selected_items
values = list(map(int, input("Enter values (profits) separated by spaces: ").split()))
weights = list(map(int, input("Enter weights separated by spaces: ").split()))
capacity = int(input("Enter knapsack capacity: "))
print("\n--- 0/1 Knapsack Process ---")
max_profit, selected_items = knapsack(weights, values, capacity)
print("Maximum Profit:", max_profit)
print("Selected Item Indices:", selected_items)
print("Selected Item Values:", [values[i] for i in selected_items])
print("Selected Item Weights:", [weights[i] for i in selected_items])