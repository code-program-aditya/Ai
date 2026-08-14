def find_min_max(arr, low, high, comparisons):
    if low == high:
        return arr[low], arr[low], comparisons
    if high == low + 1:
        comparisons += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high], comparisons
        else:
            return arr[high], arr[low], comparisons
    mid = (low + high) // 2
    min1, max1, comparisons = find_min_max(arr, low, mid, comparisons)
    min2, max2, comparisons = find_min_max(arr, mid + 1, high, comparisons)
    comparisons += 2
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)
    return overall_min, overall_max, comparisons
arr = list(map(int, input("Enter integers separated by spaces: ").split()))
print("\n--- Divide and Conquer Process ---")
minimum, maximum, comparisons = find_min_max(arr, 0, len(arr) - 1, 0)
print("Array:", arr)
print("Minimum Element:", minimum)
print("Maximum Element:", maximum)
print("Total Comparisons:", comparisons)