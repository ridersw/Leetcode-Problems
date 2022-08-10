class Solution:
    def minimumDeletions(self, s):
        stack = []
        res = 0

        for swi in s:
            if len(stack) != 0 and stack[-1] == 'b' and swi != 'b':
                stack.pop()
                res += 1
            else:
                stack.append(swi)

        return res

if __name__ == "__main__":
    obj = Solution()
    s = "aababbab"

    print(obj.minimumDeletions(s))

# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

# Example 1:

# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:m
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:

# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.
                