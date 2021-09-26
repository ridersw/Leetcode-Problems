class Solution:
	def jump(self, nums):
		
		countOfJumps = 0
		
		leftBound, rightBound = 0, 0
		
		while rightBound < len(nums)-1:
			farthest = 0
			for swi in range(leftBound, rightBound+1):
				farthest = max(farthest, swi + nums[swi])
				
			leftBound = rightBound + 1
			rightBound = farthest
			countOfJumps += 1
			
		
		return countOfJumps
		
		
if __name__ == "__main__":
	
	obj = Solution()
	
	nums = [2,3,1,1,4]
	#nums = [2,3,0,1,4]
	#nums = [0]
	#nums = [3,2,1]
	#nums = [1,1,1,1]
	nums = [2,1]
	nums = [1]
	nums = [1,2,1,1,1]
	nums = [10,9,8,7,6,5,4,3,2,1,1,0]
#	nums = [10,10,9,8,7,6,5,4,3,2,1  ]

	print(obj.jump(nums))	
	
	
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#You can assume that you can always reach the last index.

 

#Example 1:

#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

#Example 2:

#Input: nums = [2,3,0,1,4]
#Output: 2
	