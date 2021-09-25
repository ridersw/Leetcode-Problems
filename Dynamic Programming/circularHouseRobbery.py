class Solution:
	def rob(self, nums):
	
		if not nums:
			return 0
	
		if len(nums) < 4:	
			return max(nums)
			
		leaveFirst = nums[1:]
		leaveLast = nums[:-1]

		def checkAmount(nums):
			
			dp = [0] * len(nums)
			
			dp[0] = nums[0]
			dp[1] = max(nums[0], nums[1])
			
			for swi in range(2, len(nums)):
				dp[swi] = max(dp[swi - 2] + nums[swi], dp[swi-1])
				
			return max(dp)	
			
		amountLeaveFirst = checkAmount(leaveFirst)
		amountLeaveLast = checkAmount(leaveLast)
		
		#print(f'amountLeaveFirst: {amountLeaveFirst}')
		#print(f'amountLeaveLast: {amountLeaveLast}')
		
		return max(amountLeaveFirst, amountLeaveLast)
		
if __name__ == "__main__":
	obj = Solution()
	
	nums = [[2,3,2], [1,2,3,1], [1,2,3], [1,1], [200,3,140,20,10], [1,1,1,2]]
	
	for num in nums:
		print('Input:', num, '    Answer: ', obj.rob(num))

#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

#Example 1:

#Input: nums = [2,3,2]
#Output: 3
#Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

#Example 2:

#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
