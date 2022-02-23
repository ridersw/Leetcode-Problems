class Solution:
    def isOneDistanceApart(self, s, t):
        count = 0

        if abs(len(s) - len(t)) > 1:
            return False

        
        pointer1 = 0

        while pointer1 < len(s) and pointer1 < len(t):
            if s[pointer1] == s[pointer1]:
                pointer1 += 1

            else:
                return any([
                    s[pointer1+1:] == t[pointer1:], 
                    t[pointer1] + s[pointer1:]== t[pointer1:], 
                    t[pointer1] + s[pointer1+1:] == t[pointer1:]])


# Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

# A string s is said to be one distance apart from a string t if you can:

# Insert exactly one character into s to get t.
# Delete exactly one character from s to get t.
# Replace exactly one character of s with a different character to get t.
 

# Example 1:

# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:

# Input: s = "", t = ""
# Output: false
# Explanation: We cannot get t from s by only one step.
        



if __name__ == "__main__":
    obj = Solution()

    s = "ab"
    t = "acb"

    print(obj.isOneDistanceApart(s, t))