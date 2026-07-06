def merge_sort(nums):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(nums) <= 1:
        return nums
        
    # Divide: Cut the array in half
    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    
    # Conquer: Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # append left[i] to result
            result.append(left[i])
            i += 1
        else:
            # append right[j] to result
            result.append(right[j])
            j += 1
            
    # 2. If there are any elements left in the left array, append them
    result.extend(left[i:])
    
    # 3. If there are any elements left in the right array, append them
    result.extend(right[j:])
    
    return result

# Test it
nums = [5, 2, 8, 1, 9]
sorted_nums = merge_sort(nums)
print(sorted_nums) # Should print [1, 2, 5, 8, 9]