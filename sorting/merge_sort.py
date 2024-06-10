def merge_sort(arr):
    """
    Sorts the array using merge sort.
    """

    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        # Sorting left and right
        merge_sort(left)
        merge_sort(right)

        # Merging
        i = j = k = 0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i +=1
            else:
                arr[k] = right[j]
                j += 1
                
            k += 1

        # checking if any element left
        while i<len(left):
            arr[k]= left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
    return arr    