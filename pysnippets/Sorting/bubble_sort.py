def bubble_sort(dict_list, key, reverse=False):
    """Bubble sort implementation."""
    n = len(dict_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if (dict_list[j][key] > dict_list[j+1][key]) != reverse:
                dict_list[j], dict_list[j+1] = dict_list[j+1], dict_list[j]
    return dict_list
