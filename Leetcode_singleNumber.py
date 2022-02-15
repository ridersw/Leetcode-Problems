class Solution:
    def singleNumber(self, nums):
        nums.sort()
        nums.append(0)
        res = 0

        for swi in range(1, len(nums),2):
            res += nums[swi-1]
            res -= nums[swi]

        return res
        


if __name__ == "__main__":
    obj = Solution()

    print(obj.singleNumber(nums = [4,1,2,1,2]))

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1