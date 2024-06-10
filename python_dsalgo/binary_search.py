def binary_search(arr, target):
    """
    Perform a binary search on the given sorted array to find the target value.

    Parameters:
    arr (list): The sorted list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    # Initialize the starting and ending indices
    left, right = 0, len(arr) - 1

    # Loop while there is a search interval
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        
        # Check if the middle element is the target value
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1  # Ignore the left half
        else:
            right = mid - 1  # Ignore the right half

    return -1  # Return -1 if the target is not found in the array
