def is_anagram(s, t):
    if len(s) != len(t):
        return False
        
    char_count = {}
    
    # Step 1: Count characters in string 's' (Using standard if/else)
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    # Step 2: Subtract characters using string 't'
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
            
        # BLANK 1: Subtract 1 from the character's count
        # Hint: char_count[char] = char_count[char] - 1
        char_count[char] = char_count[char] - 1 
        
    # BLANK 2: What do we return if we make it through the loop without returning False?
    return True

# Test it
print(is_anagram("anagram", "nagaram")) # Should print True
print(is_anagram("rat", "car"))         # Should print False