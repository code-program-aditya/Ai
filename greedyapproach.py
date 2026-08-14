def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratios = [(values[i] / weights[i], values[i], weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])
    total_profit = 0
    selected_items = []
    print("\nProfit Ratios (value/weight):")
    for ratio, val, wt, idx in ratios:
        print(f"Item {idx}: Value={val}, Weight={wt}, Ratio={ratio:.2f}")
    for ratio, val, wt, idx in ratios:
        if capacity >= wt:
            capacity -= wt
            total_profit += val
            selected_items.append((idx, wt, val, 1.0))  # fraction = 1
        else:
            fraction = capacity / wt
            total_profit += val * fraction
            selected_items.append((idx, capacity, val * fraction, fraction))
            capacity = 0
            break
    return total_profit, selected_items
values = list(map(int, input("Enter values (profits) separated by spaces: ").split()))
weights = list(map(int, input("Enter weights separated by spaces: ").split()))
capacity = int(input("Enter knapsack capacity: "))
print("\n--- Fractional Knapsack Process ---")
max_profit, selected_items = fractional_knapsack(values, weights, capacity)
print("\nSequence of Items Selected:")
for idx, wt, val, frac in selected_items:
    print(f"Item {idx}: Taken {frac*100:.1f}% (Weight={wt}, Value={val:.2f})")
print("\nMaximum Profit:", round(max_profit, 2))