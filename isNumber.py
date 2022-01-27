import numbers
from os import symlink


class Solution:
    def isNumber(self, s):

        digit = ['0','1','2','3','4','5','6','7','8','9']

        seenDigit = False
        seenExponent = False
        seenDot = False

        for swi in range(len(s)):
            if s[swi] in digit:
                seenDigit = True
            elif s[swi] == '+' or s[swi] == '-':
                if swi != 0 and s[swi-1].lower() != 'e':
                    # print(f'returning false from 19: {s[swi-1].lower()} for char: {s[swi]}')
                    return False

            elif s[swi] == 'e' or s[swi] == 'E':
                if not seenDigit or seenExponent:
                    # print('returning false from 24')
                    return False
                else:
                    seenExponent = True
                    seenDigit= False

            elif s[swi] == '.':
                # if not seenDigit or seenExponent:
                if seenExponent or swi == len(s):
                    # print('returning false from 32')
                    return False
                else:
                    seenDot = True
            else:
                # print('returning false from 37')
                return False

        return seenDigit            


if __name__ == "__main__":
    obj = Solution()

    inputs = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

    inputs = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

    # inputs = ["-0.1", "+3.14", "4."]

    for s in inputs:
        print(f'for input: {s}:         {obj.isNumber(s)}')

# A valid number can be split up into these components (in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components (in order):

# (Optional) A sign character (either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

 

# Example 1:

# Input: s = "0"
# Output: true
# Example 2:

# Input: s = "e"
# Output: false
# Example 3:

# Input: s = "."
# Output: false
 

# Constraints:

# 1 <= s.length <= 20
# s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.