class Solution:
	def maxSubArray(self, nums):
		maxSoFar = nums[0]
		maxEndHere = 0

		for swi in range(len(nums)):
			maxEndHere += nums[swi]
			if maxSoFar < maxEndHere:
				maxSoFar = maxEndHere
				
			if maxEndHere < 0:
				maxEndHere = 0
				
		return maxSoFar		
			
		
		
if __name__ == "__main__":
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	
	obj = Solution()
	
	print(obj.maxSubArray(nums))



#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#A subarray is a contiguous part of an array.

#Example 1:

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

#Example 2:

#Input: nums = [1]
#Output: 1

#Example 3:

#Input: nums = [5,4,-1,7,8]
#Output: 23

