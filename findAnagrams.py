class Solution:
    def findAnagrams(self, s, p):
    #     pList = list(p)

    #     dict = {}

    #     for char in p:
    #         if char in dict: 
    #             dict[char] += 1
    #         else:
    #             dict[char] = 1

    #     # print(f'dict: {dict}')
    #     length = len(pList)
    #     indexArray = []
    #     for swi in range(len(s)-len(p)+1):
            
    #         if s[swi] in pList:
    #             # print(f'Letter {s[swi]} found in pList  s[swi:length]: {s[swi:length]} dict: {dict}')
    #             index = obj.isAnagram(s[swi:swi+length],dict)
    #             if index:
    #                 indexArray.append(swi)

    #     return indexArray

        

    # def isAnagram(self, string1, dictionary):
    #     tempDict = dict(dictionary)
    #     # print(f'Function Called: String1: {string1} dict: {tempDict}')
    #     for char in string1:
    #         if char in tempDict and tempDict[char] > 1:
    #             tempDict[char] -= 1
    #         elif char in tempDict and tempDict[char] == 1:
    #             tempDict.pop(char)
    #         else:
    #             return False

    #     return len(tempDict) == 0


        p = list(p)
        p.sort()
        letter = p[0]

        p = "".join(p)
        s = list(s)
        length = len(p)
        indexArray = []
        print(f'p: {p}')
        

        for swi in range(len(s)-len(p) + 1):
            temp = s[swi:swi+length]
            temp.sort()
            if temp[0] == letter:
                temp = "".join(temp)

                if temp == p:
                    indexArray.append(swi)

        return indexArray



if __name__ == "__main__":
    obj = Solution()

    print(obj.findAnagrams(s = "cbaebabacd", p = "abc"))
    print(obj.findAnagrams(s = "abab", p = "ab"))

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