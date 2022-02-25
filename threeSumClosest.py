class Solution:
    def threeSumClosest(self, nums, target):
        difference = float('inf')
        
        nums.sort()
        
        for swi in range(len(nums)):
            low, high = swi+1, len(nums)-1
            while (low < high):
                sum = nums[swi] + nums[low] + nums[high]
                if abs(target - sum) < abs(difference):
                    difference = target - sum
                if sum < target:
                    low += 1
                else:
                    high -= 1
                    
            if difference == 0:
                break
                
        return target - difference


if __name__ == "__main__":
    obj = Solution()

    print(obj.threeSumClosest(nums = [-1,2,1,-4], target = 1))

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
 

# Constraints:

# 3 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104