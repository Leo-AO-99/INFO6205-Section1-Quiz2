def binary_search_rotated(arr: list[int], target: int, rotation_index: int) -> bool:
    """
    Perform binary search on a rotated sorted array.
    
    A rotated sorted array is an array that was initially sorted in ascending order
    but then rotated at a certain pivot index.
    
    Example:
    Original sorted array: [0, 1, 2, 4, 5, 6, 7]
    Rotated at index 4: [4, 5, 6, 7, 0, 1, 2]
    Here, the rotation index 4 means that the first four elements were moved to the end.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    
    if len(arr) == 0:
        return False
    
    # TODO: Check if the rotation_index is 0, meaning the array is not rotated.
    rotation_index %= len(arr)
    if rotation_index == 0:
        left_start = 0
        left_end = len(arr) - 1
        in_left = True
    else:
        # TODO: Determine which half (before or after rotation_index) the target belongs to.
        left_start = 0
        right_start = rotation_index
        
        left_end = rotation_index - 1
        right_end = len(arr) - 1
        
        in_left = False
        if arr[left_start] <= target:
            in_left = True
    
    
    def binary_search(arr: list[int], left: int, right: int, target: int) -> bool:
        """
        Performs a binary search on a sorted array within the specified range.
        
        :param arr: List[int] - The sorted array to search in.
        :param left: int - The left boundary of the search range (inclusive).
        :param right: int - The right boundary of the search range (inclusive).
        :param target: int - The value to search for.
        :return: bool - True if the target is in the array, False otherwise.
        """
        # TODO: Implement standard binary search logic.
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    # TODO: Perform binary search on the appropriate half using the nested function.
    ret = False
    if in_left:
        ret = binary_search(arr, left_start, left_end, target)
    else:
        ret = binary_search(arr, right_start, right_end, target)
    
    return ret  # TODO: Replace this with actual return value
