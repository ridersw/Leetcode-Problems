def check(nums):
	count = 0
	
	for swi in range(len(nums)-1):
		print(f"Checking {nums[swi]} and {nums[swi+1]}")
		if nums[swi] > nums[swi+1]:
			print("Incrementing Count")
			count += 1
	
	print(f"count == 0: {count == 0}")
	print(f"count == 1: {count == 1}")
	print(f"nums[-1] <= nums[0]: {nums[-1]} {nums[0]}  {nums[-1] <= nums[0]}")
	return count == 0 or count == 1 and nums[-1] <= nums[0]
	
if __name__ == "__main__":
	#nums = [3,4,5,1,2]
	#nums = [2,1,3,4]
	nums = [1,2,3]
	#nums = [1,1,1]
	#nums = [2,1]
	print(check(nums))
	
#Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

#There may be duplicates in the original array.

#Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

#Example 1:

#Input: nums = [3,4,5,1,2]
#Output: true
#Explanation: [1,2,3,4,5] is the original sorted array.
#You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
#Example 2:

#Input: nums = [2,1,3,4]
#Output: false
#Explanation: There is no sorted array once rotated that can make nums.