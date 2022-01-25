class Solution:
    def subarraySum(self, nums, k):

        # count= 0

        # for swi in range(len(nums)):
        #     for swj in range(swi, len(nums)):
        #         if sum(nums[swi:swj+1]) == k:
        #             count += 1

        # return count

        d=  {}
        d[0] = 1
        s = 0

        count= 0

        for swi in range(len(nums)):
            s += nums[swi]

            if s-k in d:
                count += d[s-k]

            if s in d:
                d[s] += 1
            else:
                d[s] = 1

        print(f'd: {d}')
        return count

if __name__ == "__main__":
    obj = Solution()

    nums = [1,2,3]
    k = 3

    # nums = [1,1,1]
    # k = 2

    nums = [1,-1,0]
    k = 0

    nums = [1,2,1,3]
    k = 3

    print(obj.subarraySum(nums, k))

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