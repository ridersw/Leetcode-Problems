class Solution:
    def isIsomorphic(self, s, t):
        source_dict = {}
        target_dict = {}

        if len(set(s)) == len(s) and len(set(t)) == len(t):
            return True

        for swi in range(len(s)):
            if s[swi] in source_dict and source_dict[s[swi]] != t[swi]:
                return False

            if t[swi] in target_dict and target_dict[t[swi]] != s[swi]:
                return False

            source_dict[s[swi]] = t[swi]
            target_dict[t[swi]] = s[swi]

        return True
        

if __name__ == "__main__":
    obj = Solution()

    s = "egg"
    t = "add"

    s = "foo"
    t = "bar"

    s = "paper"
    t = "title"

    print(obj.isIsomorphic(s, t))

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"
# Output: true
# Example 2:

# Input: s = "foo", t = "bar"
# Output: false
# Example 3:

# Input: s = "paper", t = "title"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.