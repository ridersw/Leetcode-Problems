class Solution:
    def groupAnagrams(self, strs):
        res = {}

        for string in strs:
            sorted_string = "".join(sorted(string))

            if sorted_string not in res:
                res[sorted_string] = []
            
            res[sorted_string].append(string)

        return list(res.values())

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