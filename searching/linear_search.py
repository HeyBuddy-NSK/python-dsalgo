def linear_search(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list to search through.
    target: The value to search for.

    Returns:
    int: The index of the target if found, otherwise -1.
    """
    # Loop through each element in the array
    for index, value in enumerate(arr):
        # Check if the current element is the target value
        if value == target:
            return index  # Return the index if the target is found
    
    return -1  # Return -1 if the target is not found in the array