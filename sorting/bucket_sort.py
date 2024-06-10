def bucket_sort(arr):
    """
    Sorts the array using bucket sort.
    """

    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    bucket = []
    
    for i in range(n):
        bucket.append([])
        
    for j in arr:
        index_b = int( (j-min_val) / (max_val - min_val +1) * n )
        bucket[index_b].append(j)
        
    for i in range(n):
        bucket[i] = sorted(bucket[i])
        
    k = 0
    for i in range(n):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
            
    return arr