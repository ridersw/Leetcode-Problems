class Solution:
    def wordPattern(self, pattern, s):
        dict = {}
        pattern = list(pattern)
        s = s.split(" ")

        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False

        for swi, c in enumerate(pattern):
            if c in dict:
                if dict[c] != s[swi]:
                    return False
            else:
                dict[c] = s[swi]

        return True

if __name__ == "__main__":
    obj = Solution()
    # print(obj.wordPattern(pattern = "abba", s = "dog cat cat dog"))
    # print(obj.wordPattern(pattern = "abba", s = "dog cat cat fish"))
    # print(obj.wordPattern(pattern = "aaaa", s = "dog cat cat dog"))
    print(obj.wordPattern(pattern = "abba", s = "dog dog dog dog"))

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 

# Constraints:

# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.