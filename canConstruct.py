class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ran = {}
        
        for char in magazine:
            if char not in dict_ran:
                dict_ran[char] = 0
            dict_ran[char] += 1
            
            
        for char in ransomNote:
            if char not in dict_ran or dict_ran[char] < 1:
                return False
            dict_ran[char] -= 1
            
        return True
            
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.