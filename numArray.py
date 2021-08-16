class NumArray:
	
	def __init__(self, nums):
		self.nums = nums
		
	def sumRange(self, left, right):
		
		newArray = self.nums[left:right+1]
		print(f"newArray: {newArray}")

		return sum(newArray)	
		
		
if __name__ == "__main__":
	
	sums = [-2, 0, 3, -5, 2, -1]
	
	parameters = [[0, 2], [2, 5], [0, 5]]
	
	obj = NumArray(sums)
	
	for pairs in parameters:
		
		param_1 = obj.sumRange(pairs[0], pairs[1])
	
		print(f"Answer: {param_1}")
		
#Given an integer array nums, handle multiple queries of the following type:

#Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
#Implement the NumArray class:

#NumArray(int[] nums) Initializes the object with the integer array nums.
#int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).		