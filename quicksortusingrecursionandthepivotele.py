def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        print(f"After partition (pivot={arr[pivot_index]}): {arr}")
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
def partition(arr, low, high):
    pivot = arr[low]   # First element as pivot
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j
data = [int(x) for x in input("Enter the elements separated by spaces: ").split()]
print("Original Array:", data)
quick_sort(data, 0, len(data) - 1)
print("Sorted Array:", data)