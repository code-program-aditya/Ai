def selection_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        extreme_idx = i
        for j in range(i+1, n):
            if ascending:
                if arr[j] < arr[extreme_idx]:
                    extreme_idx = j
            else:
                if arr[j] > arr[extreme_idx]:
                    extreme_idx = j
        arr[i], arr[extreme_idx] = arr[extreme_idx], arr[i]
if __name__ == "__main__":
    arr = list(map(int, input("Enter integers separated by space: ").split()))
    arr_asc = arr.copy()
    selection_sort(arr_asc, ascending=True)
    print("Ascending order:", arr_asc)
    arr_desc = arr.copy()
    selection_sort(arr_desc, ascending=False)
    print("Descending order:", arr_desc)
    print("Time Complexity: O(n^2) for best, worst, and average cases.")