def bubble_sort(arr):
    """
    Sorts the array using bubble sort.
    """
    n = len(arr)
    
    for i in range(n):
        
        # variable to keep track if adjacent swapped or not.
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        # break if no swaps
        if not swapped:
            break
    
    return arr