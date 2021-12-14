class Solution:
    def maxPower(self, s):
        maxSoFar = 1
        curr = 1

        if not s:
            return 0

        for swi in range(len(s)-1):
            if s[swi] == s[swi+1]:
                curr += 1
            else:
                curr = 1

            maxSoFar = max(maxSoFar, curr)
        return maxSoFar

if __name__ == "__main__":
    obj = Solution()

    s = "leetcode"
    s = "abbcccddddeeeeedcba"
    s = "j"
    s = "cc"

    print(obj.maxPower(s))

# The power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Given a string s, return the power of s.

 

# Example 1:

# Input: s = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: s = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
# Example 3:

# Input: s = "triplepillooooow"
# Output: 5
# Example 4:

# Input: s = "hooraaaaaaaaaaay"
# Output: 11
