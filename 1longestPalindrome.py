class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        
        for ele in s:
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1
                
        count = 0
        
        for key, values in dict.items():
            if values % 2 == 0:
                count = count + values
                
        max_odd = 0
        
        for key, values in dict.items():
            if values % 2 != 0:
                max_odd = max(max_odd, values)
                
        count = count + max_odd
        return count

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.