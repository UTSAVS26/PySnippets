def cycle_sort(arr):
    """
    Cycle Sort algorithm

    Time complexity: O(n) in the best case, O(n^2) in the worst case
    Space complexity : O(1)

    :param arr: input array to be sorted
    :return: None
    """
    writes = 0

    # Loop through the array to find cycles to rotate
    for cycleStart in range(len(arr) - 1):
        item = arr[cycleStart]

        # Find where to put the item
        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
            if arr[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1

        # Rotate the rest of the cycle
        while pos != cycleStart:

            # Find where to put the item
            pos = cycleStart
            for i in range(cycleStart + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            # Put the item there or right after any duplicates
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

    # Check if the array is sorted
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise ValueError("Array is not sorted")
