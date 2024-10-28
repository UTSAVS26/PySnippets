def cocktail_shaker_sort(arr):
    """
    Sorts an array using the cocktail shaker sort algorithm.

    Args:
        arr (list): The list of elements to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Initialize the start and end indices
    start = 0
    end = n - 1
    swapped = True  # Flag to track if a swap occurred

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                # Swap elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # If no swaps occurred, the array is sorted
        if not swapped:
            break

        # Reduce the end boundary
        end -= 1
        swapped = False  # Reset the flag for the backward pass

        # Backward pass
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                # Swap elements
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        # Increase the start boundary
        start += 1

    return arr

# Example usage:
if __name__ == "__main__":
    sample_list = [5, 3, 8, 4, 2]
    sorted_list = cocktail_shaker_sort(sample_list)
    print("Sorted List:", sorted_list)
