from typing import final


class Solution:
    def longestPalindrome(self, s):
        finalString = ''

        for swi in range(len(s)):
            tempString1 = self.getPalindrome(s, swi, swi+1)
            tempString2 = self.getPalindrome(s, swi, swi)
            finalString = max([finalString, tempString1, tempString2], key = lambda x: len(x))

        return finalString

    def getPalindrome(self, s, left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right]: 
            left -= 1
            right += 1

        return s[left+1:right]


if __name__ == "__main__":
    obj = Solution()

    s = "babad"

    print(obj.longestPalindrome(s))

# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.