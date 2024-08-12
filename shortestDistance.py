class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = None
        index2 = None
        ans = len(wordsDict) + 2

        for swi in range(len(wordsDict)):
            if wordsDict[swi] == word1:
                index1 = swi

            if wordsDict[swi] == word2:
                index2 = swi

            # print(f'for word: {wordsDict[swi]} index1: {index1} and index2: {index2}')

            if index1 != None and index2!= None:
                # print(f'index1: {index1} and index2: {index2}')
                ans = min(ans, abs(index1 - index2))

        return ans
    
# Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

# Example 1:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
# Example 2:

# Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
 

# Constraints:

# 2 <= wordsDict.length <= 3 * 104
# 1 <= wordsDict[i].length <= 10
# wordsDict[i] consists of lowercase English letters.
# word1 and word2 are in wordsDict.
# word1 != word2