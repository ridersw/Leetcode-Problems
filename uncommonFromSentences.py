class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []  
        
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        
        for char in s1:
            if s1.count(char) == 1 and char not in s2:
                res.append(char)
                
        for char in s2:
            if s2.count(char) == 1 and char not in s1 and char not in res:
                res.append(char)
                
        return res

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
 

# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.