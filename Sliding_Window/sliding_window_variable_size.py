def min_subarray_len(arr,target):
    left  = 0
    min_len = float('inf')
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_len if min_len  != float('inf') else 0

arr = [2, 1, 5, 2, 3, 2] 
target = 7

print(min_subarray_len(arr, target))  # Output: 2