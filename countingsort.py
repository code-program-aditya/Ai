def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    print("Original Array:", arr)
    for num in arr:
        count[num - min_val] += 1
    print("Count Array (Frequency):", count)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print("Cumulative Count Array:", count)
    for num in reversed(arr):
        index = num - min_val
        output[count[index] - 1] = num
        count[index] -= 1
    print("Sorted Output Array:", output)
    return output
arr = list(map(int, input("Enter integers separated by spaces: ").split()))
print("\n--- Counting Sort Process ---")
sorted_arr = counting_sort(arr)
print("\nFinal Sorted Array:", sorted_arr)