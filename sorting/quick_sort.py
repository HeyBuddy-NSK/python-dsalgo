def quick_sort(arr):
    """
    Sorts the array using quick sort.
    """
    if len(arr)<=0:
        return arr
    
    else:
        pivot = arr[len(arr)//2]
        
        left_arr = [x for x in arr if x<pivot]
        middle_arr = [x for x in arr if x==pivot]
        right_arr = [x for x in arr if x>pivot]
        
        return quick_sort(left_arr)+middle_arr+quick_sort(right_arr)