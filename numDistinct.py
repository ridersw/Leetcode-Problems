class Solution:
	def numDistinct(self, s, t):
		memo = {}
		
		def memoization(i, j):
			
			if j == len(t):
				return 1
				
			if i == len(s):
				return 0
				
			if (i, j) in memo:
				return memo[(i, j)]
				
			
			if s[i] == t[j]:
				memo[(i, j)] = memoization(i + 1, j + 1) + memoization(i + 1, j)
			else:
				memo[(i, j)] = memoization(i + 1, j)
			
			print(f'memo: {memo}')	
			return memo[(i, j)]	
		
		return memoization(0, 0)

		
		
	
if __name__ == "__main__":
	#s = "rabbbit"
	#t = "rabbit"
	
	s = "babgbag"
	t = "bag"

	obj = Solution()

	print(obj.numDistinct(s, t))	
	
#Given two strings s and t, return the number of distinct subsequences of s which equals t.

#A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

#It is guaranteed the answer fits on a 32-bit signed integer.

#Example 1:

#Input: s = "rabbbit", t = "rabbit"
#Output: 3
#Explanation:
#As shown below, there are 3 ways you can generate "rabbit" from S.
#rabbbit
#rabbbit
#rabbbit

#Example 2:

#Input: s = "babgbag", t = "bag"
#Output: 5
#Explanation:
#As shown below, there are 5 ways you can generate "bag" from S.
#babgbag
#babgbag
#babgbag
#babgbag
#babgbag	