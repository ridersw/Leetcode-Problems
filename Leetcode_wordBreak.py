class Solution:
    def wordBreak(self, s, wordDict):
        n = len(s)
        dict = set(wordDict)

        dp = [False] * (n+1)
        dp[0] = True

        for swi in range(n):
            for swj in range(swi+1, n+1):
                if dp[swi] == True and s[swi:swj] in dict:
                    dp[swj] = True

        print(f'dp: {dp}')
        return dp[-1]
        


if __name__ == "__main__":
    obj = Solution()

    s = "leetcode"
    wordDict = ["leet","code"]

    # s = "applepenapple" 
    # wordDict = ["apple","pen"]

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]

    print(obj.wordBreak(s, wordDict))

# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false