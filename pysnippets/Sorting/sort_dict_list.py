def sort_dict_list(dict_list, key, reverse=False):
    """
    Sorts a list of dictionary by a specified key.

    Args:
        dict_list (list): A list of dictionaries to be sorted.
        key (str): The dictionary key to sort by.
        reverse (bool, optional): If True sort in descending order. Default is False (ascending order)

    Returns:
        list: A new list of dictionaries sorted by the specified key.

    Raises:
        ValueError: if the list is empty or if the specified key is not present in all dictionaries

    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
        >>> sort_dict_list(data)
        [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]
    """

    if not dict_list:
        raise ValueError("The list of dictionaries is empty.")

    if not all(key in d for d in dict_list):
        raise ValueError(f"The key {key} is not present in all dictionaries.")

    return sorted(dict_list, key=lambda x: x[key], reverse=reverse)


def bubble_sort(dict_list, key, reverse=False):
    """Bubble sort implementation."""
    n = len(dict_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if (dict_list[j][key] > dict_list[j+1][key]) != reverse:
                dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]
    return dict_list


def merge_sort(dict_list, key):
    """Merge sort implementation."""
    if len(dict_list) > 1:
        mid = len(dict_list) // 2
        left_half = dict_list[:mid]
        right_half = dict_list[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                dict_list[k] = left_half[i]
                i += 1
            else:
                dict_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            dict_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            dict_list[k] = right_half[j]
            j += 1
            k += 1

    return dict_list


def quick_sort(dict_list, key):
    """Quick sort implementation."""
    if len(dict_list) <= 1:
        return dict_list
    pivot = dict_list[len(dict_list) // 2][key]
    left = [x for x in dict_list if x[key] < pivot]
    middle = [x for x in dict_list if x[key] == pivot]
    right = [x for x in dict_list if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)


def insertion_sort(dict_list, key, reverse=False):
    """Insertion sort implementation."""
    for i in range(1, len(dict_list)):
        key_item = dict_list[i]
        j = i - 1
        while j >= 0 and (key_item[key] < dict_list[j][key]) != reverse:
            dict_list[j + 1] = dict_list[j]
            j -= 1
        dict_list[j + 1] = key_item
    return dict_list

def cocktail_sort(dict_list, key, reverse=False):
    """Cocktail sort implementation """
    n = len(dict_list)
    start = 0
    end = n - 1
    while start < end:
        new_end = start
        for i in range(start, end):
            if (dict_list[i][key] > dict_list[i + 1][key]) != reverse:
                dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                new_end = i
        end = new_end

        new_start = end
        for i in range(end - 1, start - 1, -1):
            if (dict_list[i][key] > dict_list[i + 1][key]) != reverse:
                dict_list[i], dict_list[i + 1] = dict_list[i + 1], dict_list[i]
                new_start = i
        start = new_start

    return dict_list


if __name__ == "__main__":
    data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    sorted_data = sort_dict_list(data, key="age")
    print(sorted_data)
