
def sum_two(nums, target):
    seen = {}
    for i, val in enumerate(nums):
        compliment = target - val
        
        if compliment in seen:
            return[seen[compliment],i]
            
        else:
            seen[val] = i
            
    return 'no sum found'
                
                
                
nums = [2, 7, 11, 15]
target=9
result = sum_two(nums, target)

print(result)
