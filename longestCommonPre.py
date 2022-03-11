
class Solution:
    def longestCommonPrefix(self, strs):
        char = ""
        print(f'strs: {strs}')
        strs.sort(key = len)
        length = len(strs[0])
        print(f'strs: {strs}')
        pre = ""
        for swi in range(length):
            print(f'checking for character: {strs[0][swi]}')
            for swj in range(len(strs)):
                if strs[swj][swi] != strs[0][swi]:
                    return pre
            
            pre += strs[0][swi]
        
        return pre
        

if __name__ == "__main__":
    obj = Solution()

    print(obj.longestCommonPrefix(strs = ["flower","flow","flight"]))
    print(obj.longestCommonPrefix(strs = ["dog","racecar","car"]))

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lower-case English letters.

