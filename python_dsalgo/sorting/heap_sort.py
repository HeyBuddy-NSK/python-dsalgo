def heapify(arr,n,i):
    """
    Function to maintain the heap property of a subtree rooted at index i,
    assuming the subtrees are already heaps.
    """
    largest = i
    left = 2*i+1
    right = 2*i+2
    
    if left<n and arr[largest]<arr[left]:
        largest = left
        
    if right<n and arr[largest]<arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)
        

def heap_sort(arr):
    """
    Sorts the array using heap sort.
    """
    n = len(arr)
    
    # building a max heap - This process ensures that the largest element is at the root of the heap.
    for i in range(n//2-1,-1,-1): # this range function will give numbers in reverse like 5, 4, 3, 2, 1, 0.
        heapify(arr,n,i)
        
    # sorting the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)
        
    return arr