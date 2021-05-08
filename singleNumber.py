def singleNumber(nums):
	
	#for item in nums:
	#	if nums.count(item) == 1:
	#		return item
	#		
	#return nums[0]
	
	if len(nums) == 1:
		return nums[0]
	
	dict = {}
	
	for item in nums:
		if item in dict:
			dict[item] += 1
		else:
			dict[item] = 1
			
	for key, values in dict.items():
		if values == 1:
			return key
			
	
	
if __name__ == "__main__":
	print(singleNumber([-1,-1,-2]))
	
#Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

#Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

#Example 1:

#Input: nums = [2,2,1]
#Output: 1
#Example 2:

#Input: nums = [4,1,2,1,2]
#Output: 4
#Example 3:

#Input: nums = [1]
#Output: 1