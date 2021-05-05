def firstMissingPositive(nums):

	for swi in range(1, max(nums)+2):
		#print(f"swi: {swi}")
		if swi not in nums:
			return swi
	
if __name__ == "__main__":
	print(firstMissingPositive([1,2,0]))
	print(firstMissingPositive([3,4,-1,1]))
	
#Given an unsorted integer array nums, find the smallest missing positive integer.

#Example 1:

#Input: nums = [1,2,0]
#Output: 3
#Example 2:

#Input: nums = [3,4,-1,1]
#Output: 2
#Example 3:

#Input: nums = [7,8,9,11,12]
#Output: 1