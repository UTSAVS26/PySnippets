
def flatten_list(nested_list):
    flat_list = []
    
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))  # Recursive call for nested lists
        else:
            flat_list.append(item)
    
    return flat_list
