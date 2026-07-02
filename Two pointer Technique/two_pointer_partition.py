def move_zeroes(arr):
    insert = 0   # boundary: everything before insert is non-zero

    for curr in range(len(arr)):
        if arr[curr] != 0:
            arr[insert], arr[curr] = arr[curr], arr[insert]
            insert += 1