class Solution:
	def countBits(self, n):
	
		array = [0] * (n+1)
		
		for swi in range(n+1):
			#ans = convertBinary(swi)
			ans = "{0:b}".format(swi)
			array[swi] = ans.count("1")
	
		
		return array
		
if __name__ == "__main__":
	obj = Solution()

	print(obj.countBits(5))
	
#Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

#Example 1:

#Input: n = 2
#Output: [0,1,1]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10
#Example 2:

#Input: n = 5
#Output: [0,1,1,2,1,2]
#Explanation:
#0 --> 0
#1 --> 1
#2 --> 10
#3 --> 11
#4 --> 100
#5 --> 101	