def shell_sort(arr):
    """
    Sorts the array using shell sort.
    """

    n = len(arr)
    gap = len(arr)//2
    
    while gap>0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap]>temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2
        
    return arr