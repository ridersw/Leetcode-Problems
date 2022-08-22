class Solution:
    def maxSubArray(self, nums):
        
        array = [nums[0]]
        
        for swi in range(1, len(nums)):
            array.append(max(array[swi-1] + nums[swi], nums[swi]))

        print(f'Array: {array}')

        return max(array)

if __name__ == "__main__":
    obj = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    nums = [5,4,-1,7,8]

    print(obj.maxSubArray(nums))

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
            
            
        