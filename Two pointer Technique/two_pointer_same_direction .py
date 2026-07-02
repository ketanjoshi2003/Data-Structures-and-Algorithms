def remove_duplicates(arr):
    if not arr:
        return 0

    slow = 0   # points to last unique element placed

    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:   # found a new unique element
            slow += 1
            arr[slow] = arr[fast]    # place it after last unique

    return slow + 1