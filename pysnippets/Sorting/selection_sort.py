def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    # Input: space-separated integers
    input_data = input("Enter numbers to sort, separated by spaces: ")
    arr = list(map(int, input_data.split()))
    
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
