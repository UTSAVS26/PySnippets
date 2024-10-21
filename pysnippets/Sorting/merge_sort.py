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
