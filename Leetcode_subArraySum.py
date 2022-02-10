class Solution:
    def subarraySum(self, nums, k):
        dict = {}
        dict[0] = 1

        s, count = 0, 0

        for swi in range(len(nums)):
            # print(f'================================================')
            # print(f'For Loop: {swi+1} ')
            s += nums[swi]
            # print(f'Value of s: {s}')
            if s - k in dict:
                # print(f's-k found in dict: {s-k}')
                count += dict[s-k]

            if s in dict:
                # print(f'Updated Value of s in dict: {dict[s]}')
                dict[s] += 1
            else:
                dict[s] = 1
            #     print(f'Adding new Value of s in dict: {dict[s]}')

            # print(f'dict: {dict}')

        return count



if __name__ == "__main__":
    obj = Solution()

    print(obj.subarraySum(nums = [1,2,3], k = 3))

# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107