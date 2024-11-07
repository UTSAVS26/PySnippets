from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """
    Executes a linear search on a list to find a target element.

    Args:
        arr (List[int]): The list of elements to search through.
        target (int): The element to search for within the list.

    Returns:
        int: The index of the target element if found; otherwise, -1.
    """
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10

    # Function call
    result = linear_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print(f"Element is present at index {result}")