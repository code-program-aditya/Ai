def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons
arr = list(map(int, input("Enter integers separated by spaces: ").split()))
target = int(input("Enter the element to search: "))
print("\n--- Linear Search Process ---")
position, comparisons = linear_search(arr, target)
if position != -1:
    print(f"Element {target} found at position {position} (0-based index).")
else:
    print(f"Element {target} not found in the array.")
print("Total Comparisons Performed:", comparisons)