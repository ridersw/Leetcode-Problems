class Solution:
    def threeSum(self, nums):
    #     nums = sorted(nums)
    #     result = set()
    #     for i in range(len(nums)):
    #         l = i + 1
    #         r = len(nums) - 1
    #         target = 0 - nums[i]
    #         while l < r:
    #             if nums[l] + nums[r] == target:
    #                 result.add((nums[i], nums[l], nums[r]))
    #                 l += 1
    #                 r -= 1
    #             elif nums[l] + nums[r] < target:
    #                 l += 1
    #             else:
    #                 r -= 1
    #     return list(result)

        nums = sorted(nums)

        res = set()
        
        for swi in range(len(nums)):
            left = swi+1
            right = len(nums)-1

            target = 0 - nums[swi]

            while left < right:
                if nums[left] + nums[right] == target:
                    res.add((nums[swi], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return list(res)

if __name__ == "__main__":
    
    obj = Solution()
    nums = [-1,0,1,2,-1,-4]

    print(obj.threeSum(nums))

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []
 