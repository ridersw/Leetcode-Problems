class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer1 = 0
        pointer2 = len(nums)-1
        
        if len(nums) < 2:
            return nums
        
        while pointer1 <= pointer2:
            while nums[pointer1] % 2 == 0 and pointer1 < len(nums)-1:
                pointer1 += 1
                
            while nums[pointer2] % 2 != 0 and pointer2 > 0:
                pointer2 -= 1
                
            
                
            if pointer1 < pointer2:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
            else:
                return nums
            
        return nums
        
# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000