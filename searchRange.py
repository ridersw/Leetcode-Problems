def searchRange(nums, target):
	
	if nums.count(target) < 1:
		return [-1, -1]
	
	index1 = nums.index(target)
	print("Index1: ", index1)
	
	nums = nums[::-1]
	
	index2 = nums.index(target)
	print("Index2: ", index2)
	index2 = len(nums) - (index2 + 1)
	
	return [index1, index2]
	
if __name__ == "__main__":
	nums = [1]
	#nums = [5,7,7,8,8,10]
	target = 1
	#target = 8
	numLoc = searchRange(nums, target)
	print("Locations: ", numLoc)
	
	
#My Solution Test	
#[5,7,7,8,8,10] -> 3 
#[10,8,8,7,7,5] -> 1


#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]


