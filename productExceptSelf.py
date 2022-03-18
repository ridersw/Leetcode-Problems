class Solution:
    def productExceptSelf(self, nums):
        left, right= [0]*len(nums), [0]*len(nums)
        left[0] = 1
        right[-1] = 1

        for swi in range(1, len(nums)):
            left[swi] = (left[swi-1] * nums[swi-1])

        for swi in range(len(nums)-2, -1, -1):
            right[swi] = right[swi+1] * nums[swi+1]

        print(f'left: {left}')
        print(f'right: {right}')

        res = []

        for swi in range(len(nums)):
            res.append(left[swi] * right[swi])

        return res


if __name__ == "__main__":  
    obj = Solution()
    #print(obj.productExceptSelf(nums = [1,2,3,4]))
    print(obj.productExceptSelf(nums = [-1,1,0,-3,3]))

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.