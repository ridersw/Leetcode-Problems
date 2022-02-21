class Solution:
    def majorityElement(self, nums):
        length = (len(nums))/ 2
        # print(f'length: {length}')

        # for ele in nums:
        #     print(f'checking for {ele} and count: {nums.count(ele)}')
        #     if nums.count(ele) >= length:
        #         return ele

        dict = {}

        for ele in nums:
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1

        for key, value in dict.items():
            if value >= length:
                return key

if __name__ == "__main__":
    obj = Solution()


    print(obj.majorityElement(nums = [6,5,5]))

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -231 <= nums[i] <= 231 - 1