class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        finalLength = 1
        tempStr = ""
        
        for swi in range(len(s)):
            if s[swi] not in tempStr:
                tempStr += s[swi]
            else:
                finalLength = max(finalLength, len(tempStr))
                tempIndex = tempStr.index(s[swi])
                tempStr = tempStr[tempIndex+1:] + s[swi]
                
        finalLength = max(finalLength, len(tempStr))
        return finalLength

# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.