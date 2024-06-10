def selection_sort(arr):
    """
    Sorts the array using selection sort.
    """
    n = len(arr)
    
    for i in range(n):
        # to find minimum element in the unsorted region
        min_index = i
        
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j
                
        # Swapping the minimum element found with first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        
    return arr