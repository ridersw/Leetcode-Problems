import math

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)

        limit = 10000
        result = 0

        for swi in range(limit):
            swi = str(swi)
            swi = swi + swi[::-1]
            p = int(swi)
            p2 = p ** 2
            if p2 > right:
                break

            if p2 > left and self.is_pal(p2):
                result += 1

        for swi in range(1, limit):
            swi = str(swi)
            swi = swi + swi[::-1][1:]
            p = int(swi)
            p2 = p ** 2
            if p2 > right:
                break

            if p2 >= left and self.is_pal(p2):
                result += 1

        return result

    def is_pal(self, n):
        n = str(n)
        if n == n[::-1]:
            return True
        return False



if __name__ == "__main__":
    obj = Solution()

    print(obj.superpalindromesInRange(4, 1000))

# Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

# Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

# Example 1:

# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
# Example 2:

# Input: left = "1", right = "2"
# Output: 1
 

# Constraints:

# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 1018 - 1].
# left is less than or equal to right.