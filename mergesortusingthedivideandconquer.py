def merge_sort(arr, level=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        print("  " * level + f"Dividing: {arr}")
        merge_sort(left_half, level + 1)
        merge_sort(right_half, level + 1)
        i = j = k = 0
        print("  " * level + f"Merging: {left_half} and {right_half}")
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        print("  " * level + f"After Merge: {arr}")
    return arr
data = [38, 27, 43, 3]
print("Original Array:", data)
sorted_array = merge_sort(data.copy())
print("Sorted Array:", sorted_array)