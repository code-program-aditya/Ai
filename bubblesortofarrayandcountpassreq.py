def bubble_sort(arr):
    n = len(arr)
    passes = 0
    for i in range(n - 1):
        swapped = False
        # Inner loop for comparisons
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        passes += 1
        if not swapped:
            break
    return arr, passes

arr = list(map(int, input("Enter integers separated by spaces: ").split()))
sorted_arr, total_passes = bubble_sort(arr)
print("\nSorted Array:", sorted_arr)
print("Total Passes Required:", total_passes)