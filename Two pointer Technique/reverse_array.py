def reverse_array(s):
    
    left = 0
    right = len(s) - 1
    
    while left < right :
        s[left] , s[right] = s[right], s[left] 
        right -=1
        left +=1
    return s
    
s = ['h', 'e', 'l', 'l', 'o']
reverse_array(s)
print(s) # Should print ['o', 'l', 'l', 'e', 'h']