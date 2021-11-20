class Solution:
    def minJump(self, nums):

        if len(nums) == 1:
            return 0

        jumpCount = 0
        curr, farthest = 0,0 

        for swi in range(len(nums)-1):
            if swi + nums[swi] > farthest:
                farthest = swi + nums[swi]

            if curr == swi:
                jumpCount += 1
                curr = farthest

        return jumpCount

if __name__ == "__main__":
    obj = Solution()

    nums=  [2,3,1,1,4]
    #nums=  [2,0,0,1,4]

    print(obj.minJump(nums))

# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2