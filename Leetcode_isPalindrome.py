from ctypes import pointer
from curses.ascii import isalnum


class Solution:
    def isPalindrome(self, s):


        # allowedCharacters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        
        # res = ""
        # s = s.lower()

        # for char in s:
        #     if char in allowedCharacters:
        #         res += char

        # return res == res[::-1]

        pointer1, pointer2 = 0, len(s)-1

        while pointer1 < pointer2:
            while pointer1 < pointer2 and not s[pointer1].isalnum():
                pointer1 += 1
            while pointer2 > pointer1 and not s[pointer2].isalnum():
                pointer2 -= 1
            
            if s[pointer1].lower() != s[pointer2].lower():
                return False

            pointer1 += 1
            pointer2 -= 1

        return True


if __name__ == "__main__":
    obj = Solution()

    print(obj.isPalindrome(s = "A man, a plan, a canal: Panama"))

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.