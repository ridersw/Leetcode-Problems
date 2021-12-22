class Solution:
    def canConvert(self, str1, st2):
        alreadyDone = {}

        for swi in range(len(str1)):
            if str1[swi] in alreadyDone:
                if alreadyDone[str1[swi]] != str2[swi]:
                    return False
            else:
                alreadyDone[str1[swi]] = str2[swi]

        return True
 

if __name__ == "__main__":
    obj = Solution()

    str1 = "aabcc"
    str2 = "ccdee"

    str1 = "leetcode"
    str2 = "codeleet"

    print(obj.canConvert(str1, str2))

# Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

# In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

# Return true if and only if you can transform str1 into str2.

 

# Example 1:

# Input: str1 = "aabcc", str2 = "ccdee"
# Output: true
# Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.
# Example 2:

# Input: str1 = "leetcode", str2 = "codeleet"
# Output: false
# Explanation: There is no way to transform str1 to str2.