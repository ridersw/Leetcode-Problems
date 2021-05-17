def checkPossibility(nums):
	
	#count = 0
	
	#for swi in range(len(nums)-1):
	#	if nums[swi] >	 min(nums[swi+1:]):
	#		count += 1
	#		if count > 1:
	#			return False
	
	#return True
	
	#length = len(nums)
	#for i in range(0, length):
	#	left_half = nums[:i]
	#	right_half = nums[i+1:]
	#	new_nums = left_half + right_half
            
	#	if all(new_nums[i] <= new_nums[i+1] for i in range(len(new_nums)-1)):
	#		return True
	#return False
	
	for swi in range(len(nums)):
		tempNumFirst = nums[:swi]
		tempNumSecond = nums[swi+1:]
		tempNum = tempNumFirst + tempNumSecond
		
		if all(tempNum[swi] <= tempNum[swi+1] for swi in range(len(tempNum)-1)):
			return True
		
	return False	
	
if __name__ == "__main__":
	print(checkPossibility(nums = [4,2,3]))
	print(checkPossibility(nums = [4,2,1]))
	print(checkPossibility(nums = [3,4,2,3]))
	print(checkPossibility(nums = [5,7,1,8]))
	
#Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

#We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

#Example 1:

#Input: nums = [4,2,3]
#Output: true
#Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#Example 2:

#Input: nums = [4,2,1]
#Output: false
#Explanation: You can't get a non-decreasing array by modify at most one element.