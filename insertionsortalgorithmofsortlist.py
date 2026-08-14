def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            swaps += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    return arr, comparisons, swaps

arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split(',')))
sorted_arr, comp, swp = insertion_sort(arr)
print("Sorted array:", sorted_arr)
print("Total comparisons:", comp)
print("Total swaps:", swp)