def quick_sort(dict_list, key):
    """Quick sort implementation."""
    if len(dict_list) <= 1:
        return dict_list
    pivot = dict_list[len(dict_list) // 2][key]
    left = [x for x in dict_list if x[key] < pivot]
    middle = [x for x in dict_list if x[key] == pivot]
    right = [x for x in dict_list if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)
