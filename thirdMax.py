def thirdMax(nums):
	print(f"nums: {nums}")
	
	nums = set(nums)
	
	print(f"nums: {nums}")
	
	nums = list(nums)
	
	print(f"nums: {nums}")
	
	nums.sort(reverse = True)
	
	print(f"nums: {nums}")
	
	if len(nums) >= 3:
		return nums[2]
	else:
		return max(nums)
	
if __name__ == "__main__":
	nums = [3,2,1, 1]
	print(thirdMax(nums))
	
	
	
#Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

#Example 1:

#Input: nums = [3,2,1]
#Output: 1
#Explanation: The third maximum is 1.

#Example 2:

#Input: nums = [1,2]
#Output: 2
#Explanation: The third maximum does not exist, so the maximum (2) is returned instead.