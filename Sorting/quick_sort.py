def quick_sort(nums):
    # 1. Base case: if len(nums) <= 1, return nums
    if len(nums) <= 1:
        return nums
    # 2. Pick pivot (middle element)
    pivot = len(nums) // 2
    mid = nums[pivot]
    
    # 3. Create left, middle, right lists
    left = []
    middle = []
    right = []

    # 4. Loop through nums and put elements in the 3 lists
    
    for i in nums:
        if i < mid:
            left.append(i)
        elif i > mid:
            right.append(i)
        else:
            middle.append(i)
    
    # 5. Return quick_sort(left) + middle + quick_sort(right)
    return quick_sort(left) + middle + quick_sort(right)

# Test it
nums = [5, 2, 8, 1, 9]
sorted_nums = quick_sort(nums)
print(sorted_nums) # Should print [1, 2, 5, 8, 9]