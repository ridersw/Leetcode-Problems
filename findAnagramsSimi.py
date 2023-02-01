from collections import Counter

class Solution:
    def findAnagrams(self, s, p):

        result = []

        dict_s = Counter(s[:len(p)])
        dict_p = Counter(p)

        first_pointer = 0
        last_pointer = len(p)

        while last_pointer <= len(s):
            if dict_s == dict_p:
                result.append(first_pointer)

            dict_s[s[first_pointer]] -= 1

            if dict_s[s[first_pointer]] <= 0:
                dict_s.pop(s[first_pointer])

            if last_pointer < len(s):
                dict_s[s[last_pointer]] += 1

            first_pointer += 1
            last_pointer += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    print(obj.findAnagrams(s = "cbaebabacd", p = "abc"))

# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.