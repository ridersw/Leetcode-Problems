class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dictt = {}

        for ele in s:
            if ele not in dictt:
                dictt[ele] = 0
            dictt[ele] += 1

        odd = 0

        for key, values in dictt.items():
            if values % 2 != 0:
                odd += 1


            if odd > 1:
                return False

        return True
    
# Given a string s, return true if a permutation of the string could form a 
# palindrome
#  and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.