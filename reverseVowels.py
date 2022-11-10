class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        left = 0
        right = len(s)-1
        
        s = list(s)
        
        while left < right:
            while s[left] not in vowels and left < right:
                left += 1
            # print(f'Found Vowel at {left} : {s[left]}')
            while s[right] not in vowels and right > left:
                right -= 1
            # print(f'Found Vowel at {right} : {s[right]}')   
            s[left], s[right] = s[right],s[left]
            
            left += 1
            right -= 1
            
        return "".join(s)

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.