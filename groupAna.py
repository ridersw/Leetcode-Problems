from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        result = {}

        for char in strs:
            temp = "".join(sorted(char))
            if temp not in result:
                result[temp] = []
            result[temp].append(char)

        return result.values()
            
            

if __name__ == "__main__":
    obj = Solution()

    print(obj.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.