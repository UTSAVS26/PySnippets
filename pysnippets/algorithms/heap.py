def heapify(arr, n, i):
    """
    Converts a subtree rooted with node i into a max heap.
    
    Args:
        arr (list): The array representation of the heap.
        n (int): The size of the heap.
        i (int): The index of the root of the subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest element so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Performs heap sort on a given array.
    
    Args:
        arr (list): The array to be sorted.
    
    Returns:
        list: The sorted array.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Call heapify on the reduced heap

    return arr

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    sorted_arr = heap_sort(arr)
    print("Sorted array:", sorted_arr)
