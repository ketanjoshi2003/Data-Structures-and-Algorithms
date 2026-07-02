def remove_duplicates(nums):
    
    left = 1
    
    for right in range(1, len(nums)):
        if nums[right] != nums[right-1]:
            nums[left] = nums[right]
            left +=1
    return left
            
    
nums = [1, 1, 2, 3, 3, 4, 4, 4, 4]
length = remove_duplicates(nums)
print(nums[:length]) # Should print [1, 2, 3, 4]
print(length)        # Should print 4