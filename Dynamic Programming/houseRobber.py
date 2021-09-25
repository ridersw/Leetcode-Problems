class Solution:
	def rob(self,nums):
		
		dp = [0] * len(nums)
		
		dp[0] = nums[0]
		dp[1] = max(nums[0], nums[1])
		
		
		for swi in range(2, len(nums)):
			dp[swi] = max(dp[swi-2] + nums[swi], dp[swi-1])
			
			
		return max(dp)
		

if __name__ == "__main__":
	nums = [1, 2, 3, 1]
	nums = [2, 7, 9, 3, 1]
	nums = [2, 1, 1, 2]
	
	#dp = [2, 2, 3, 4]

	obj = Solution()

	print(obj.rob(nums))