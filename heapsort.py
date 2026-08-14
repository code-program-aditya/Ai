def heapify(arr, n, i, depth=0):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, depth + 1)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Heap after heapify at index {i}: {arr}")
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)
        print(f"Heap after removing max element: {arr}")
    return arr
arr = list(map(int, input("Enter integers separated by spaces: ").split()))
print("\n--- Heap Sort Process ---")
sorted_arr = heap_sort(arr)
print("\nFinal Sorted Array:", sorted_arr)