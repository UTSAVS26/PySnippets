def insertion_sort(dict_list, key, reverse=False):
    """Performs an insertion sort on a list of dictionaries based on a specified key."""
    for i in range(1, len(dict_list)):
        key_item = dict_list[i]
        j = i - 1
        # Adjust comparison based on the reverse flag
        if reverse:
            while j >= 0 and dict_list[j][key] < key_item[key]:
                dict_list[j + 1] = dict_list[j]
                j -= 1
        else:
            while j >= 0 and dict_list[j][key] > key_item[key]:
                dict_list[j + 1] = dict_list[j]
                j -= 1
        dict_list[j + 1] = key_item
    return dict_list
