class Solution:
	def rob(self, nums):
	
		if len(nums) < 2:
			return max(nums)
			
		if len(nums) == 3:
			return max(nums)
		
		dp = [0] * len(nums)
		
		dp[0] = nums[0]
		
		if nums[0] > nums[1]:
			dp[1] = nums[0]
			length = len(nums)-1
		else:
			dp[1] = nums[1]
			length = len(nums)	
		
		#dp[1] = max(nums[0], nums[1])
		
		#if dp[1] == nums[0]:
		#	print(f'dp[1] == nums[1]: {dp[1] == nums[1]}')
		#	length = len(nums) -1 
		#else:
		#	length = len(nums)
			
		#print(f'length: {length} ')	
		#print(dp)	
		for swi in range(2, length):
			
			dp[swi] = max(dp[swi-2] + nums[swi], dp[swi]-1)
			#print(dp)
			
		return max(dp)	
			
		
		
if __name__ == "__main__":
	obj = Solution()

	nums = [2,3,2]
	print(obj.rob(nums))
	nums = [1,2,3,1]
	print(obj.rob(nums))
	nums = [1,2,3]
	print(obj.rob(nums))
	nums = [1,1]
	print(obj.rob(nums))
	nums = [200,3,140,20,10]
	print(obj.rob(nums))
	nums = [1,1,1,2]
	print(obj.rob(nums))