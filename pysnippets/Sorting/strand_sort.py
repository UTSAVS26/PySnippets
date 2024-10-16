def strand_sort(ip): 
    # Define a helper function to merge two sorted lists 
    def merge_lists(list1, list2): 
        result = [] 
        while list1 and list2: 
            if list1[0] < list2[0]: 
                result.append(list1.pop(0)) 
            else: 
                result.append(list2.pop(0)) 
        result += list1 
        result += list2 
        return result 
  
    # Base case: if the input list has 1 or fewer elements, it's already sorted 
    if len(ip) <= 1: 
        return ip 
  
    # Initialize a sublist with the first element of the input list 
    sublist = [ip.pop(0)] 
  
    i = 0
    while i < len(ip): 
        # If the current element in the input list is greater than the last element in the sublist, 
        # add it to the sublist; otherwise, continue to the next element in the input list. 
        if ip[i] > sublist[-1]: 
            sublist.append(ip.pop(i)) 
        else: 
            i += 1
  
    # The sorted_sublist contains the sorted elements from the current sublist 
    sorted_sublist = sublist 
  
    # Recursively sort the remaining part of the input list 
    remaining_list = strand_sort(ip) 
  
    # Merge the sorted sublist and the sorted remaining_list 
    return merge_lists(sorted_sublist, remaining_list) 

