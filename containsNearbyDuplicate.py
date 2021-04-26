def containsNearbyDuplicate(nums, k):

	if len(set(nums)) == len(nums):
		return False
		
	dict = {}
	
	for i, value in enumerate(nums):
		if value in dict and abs(i - dict[value]) <= k:
			return True
		dict[value] = i
			
			
	
	#for swi in range(len(nums)):
	#	if nums.count(nums[swi]) > 1:
	#		if nums[swi] in nums[swi+1:swi+k+1]:
	#			return True
			
			
	return False
	
if __name__ == "__main__":
	nums = [1,2,3,1]
	k = 3
	
	#nums = [1,0,1,1]
	#k = 1
	
	#nums = [1,2,3,1,2,3]
	#k = 2
	#nums = [1,2,3,1,2,3]
	#k = 2
	
	
	print(containsNearbyDuplicate(nums, k))
	
#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

#Example 1:

#Input: nums = [1,2,3,1], k = 3
#Output: true
#Example 2:

#Input: nums = [1,0,1,1], k = 1
#Output: true
#Example 3:

#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false