def kLengthApart(nums, k):
	indices = []
	
	for swi in range(len(nums)):
		if nums[swi] == 1:
			indices.append(swi)
			
	print(f"indices: {indices}")
	for swi in range(len(indices)-1):
		#print(f"indices[swi+1] - indices[swi]: {indices[swi+1] - indices[swi]}")
		if indices[swi+1] - indices[swi] < (k+1):
			return False
		
	return True

if __name__ == "__main__":
	nums = [1,0,0,0,1,0,0,1]
	k = 2
	
	#nums = [1,0,0,1,0,1]
	#k = 2
	
	nums = [1,1,1,1,1]
	k = 0
	
	nums = [0,1,0,1]
	k = 1
	print(kLengthApart(nums, k))
	
#Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

#Example 1:

#Input: nums = [1,0,0,0,1,0,0,1], k = 2
#Output: true
#Explanation: Each of the 1s are at least 2 places away from each other.
#Example 2:

#Input: nums = [1,0,0,1,0,1], k = 2
##Output: false
#Explanation: The second 1 and third 1 are only one apart from each other.
#Example 3:

#Input: nums = [1,1,1,1,1], k = 0
#Output: true