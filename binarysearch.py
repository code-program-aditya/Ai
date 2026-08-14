def binary_search(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        print(f"Checking mid-element at index {mid}: {arr[mid]}")
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, high, target)
    else:
        return -1
arr = list(map(int, input("Enter sorted integers separated by spaces: ").split()))
target = int(input("Enter the element to search: "))
print("\n--- Binary Search Process ---")
position = binary_search(arr, 0, len(arr) - 1, target)
if position != -1:
    print(f"\nElement {target} found at position {position} (0-based index).")
else:
    print(f"\nElement {target} not found in the array.")