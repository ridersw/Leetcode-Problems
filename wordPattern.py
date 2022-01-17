class Solution:
    def wordPattern(self, pattern, s):
        wordP = {}
        words = s.split(" ")

        if len(pattern) != len(s) or len(set(pattern)) != len(s) or len(set(s)) != len(pattern):
            return False

        for swi, c in enumerate(pattern):
            if c in wordP:
                if wordP[c] != words[swi]:
                    return False
            else:
                wordP[c] = words[swi]

        return True

if __name__ == "__main__":
    obj = Solution()
    pattern = "abba"
    s = "dog cat cat dog"

    pattern = "abba"
    s = "dog cat cat fish"

    pattern = "aaaa"
    s = "dog cat cat dog"

    pattern = "abba"
    s = "dog dog dog dog"

    print(obj.wordPattern(pattern, s))

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