def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1     # sum too small, move left pointer right
        else:
            right -= 1    # sum too big, move right pointer left

    return []

# Test
arr = [2, 7, 11, 15]
target = 9
print(two_sum_sorted(arr, target))