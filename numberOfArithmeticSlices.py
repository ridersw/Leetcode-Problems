


class Solution:
    def numberOfArithmeticSlices(self, nums):
        le = len(nums)
        l = [0] * le
        
        for swi in range(2, le):
            if nums[swi] - nums[swi-1] == nums[swi-1] - nums[swi-2]:
                l[swi] = 1 + l[swi-1]
                
        print(l)
        return sum(l)


if __name__ == "__main__":
    obj = Solution()
    # print(obj.numberOfArithmeticSlices(nums = [1,2,3,4]))
    # print(obj.numberOfArithmeticSlices(nums = [1]))
    print(obj.numberOfArithmeticSlices(nums=[1,2,3,8,9,10]))

# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
# Example 2:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000