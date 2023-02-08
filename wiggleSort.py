class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        
        # if len(nums) == 3:
        #     nums[1], nums[2] = nums[2], nums[1]
            
        # else:
        for swi in range(1, len(nums)-1, 2):
            nums[swi], nums[swi+1] = nums[swi+1], nums[swi]
            

# Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

# You may assume the input array always has a valid answer.

 

# Example 1:

# Input: nums = [3,5,2,1,6,4]
# Output: [3,5,1,6,2,4]
# Explanation: [1,6,2,5,3,4] is also accepted.
# Example 2:

# Input: nums = [6,6,5,6,3,8]
# Output: [6,6,5,6,3,8]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# 0 <= nums[i] <= 104
# It is guaranteed that there will be an answer for the given input nums.