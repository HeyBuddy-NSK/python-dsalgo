def insertion_sort(arr):
    """
    Sorts the array using insertion sort.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        # moving elements or arr[0 to i-1] that are greater than key, to one position ahead of their current position.
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr