def fibonacci_search(arr, target):
    """
    Fibonacci search algorithm.
    :param arr: Sorted list of elements to search through.
    :param target: The element to search for.
    :return: The index of the element if found, else -1.
    """
    if not arr:  # Check for empty array
        return -1
    n = len(arr)
    fib_mm2, fib_mm1, fib_m = 0, 1, 1  # (m-2)'th, (m-1)'th, m'th Fibonacci numbers

    while fib_m < n:
        fib_mm2, fib_mm1, fib_m = fib_mm1, fib_m, fib_mm2 + fib_mm1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_mm2, n - 1)

        if arr[i] < target:
            fib_m, fib_mm1, fib_mm2, offset = fib_mm1, fib_mm2, fib_m - fib_mm1, i
        elif arr[i] > target:
            fib_m, fib_mm1, fib_mm2 = fib_mm2, fib_mm1 - fib_mm2, fib_m - fib_mm1
        else:
            return i

    if fib_mm1 and arr[offset + 1] == target:
        return offset + 1

    return -1

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = fibonacci_search(arr, target)
    if result == -1:
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
