def selection_sort(dict_list, key, reverse=False):
    
    """Selection sort implementation."""
    
    n = len(dict_list)

    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if (dict_list[j][key] < dict_list[min_index][key]) != reverse:
                min_index = j

        dict_list[min_index][key], dict_list[i][key] = dict_list[i][key], dict_list[min_index][key]


    return dict_list    