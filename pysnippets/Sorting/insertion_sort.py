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
