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

