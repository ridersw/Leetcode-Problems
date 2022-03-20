class Solution:
    def findMaxConsecutiveOnes(self, nums):
        # curr_ones, max_so_far = 0, 0
        # foundZero = False

        # for swi in range(len(nums)):
        #     #print(f'Checking for {nums[swi]} curr_ones: {curr_ones} max_so_far: {max_so_far}')
        #     if nums[swi] == 1:
        #         curr_ones += 1
        #         max_so_far = max(max_so_far, curr_ones)
        #     else:
        #         if not foundZero:
        #             curr_ones += 1
        #             max_so_far = max(max_so_far, curr_ones)
        #             foundZero = True
        #         else:
        #             max_so_far = max(max_so_far, curr_ones)
        #             curr_ones = 0
        #             foundZero = False

        # max_so_far = max(max_so_far, curr_ones)
        # return max_so_far

        ln = len(nums)
        if ln == 1:
            return 1

        if 0 not in nums:
            return ln

        zero_index = [-1]

        for swi in range(len(nums)):
            if nums[swi] == 0:
                zero_index.append(swi)

        zero_index.append(ln)
        n = len(zero_index)
        print(f'zero_index: {zero_index}')
        res=  0

        #cprint(f'zero_index: {zero_index}')

        for swi in range(n-1):
            res = max(res, (zero_index[swi+1] - zero_index[swi]) + (zero_index[swi] - zero_index[swi-1]) - 1)

        return res

if __name__ == "__main__":
    obj = Solution()
    #print(obj.findMaxConsecutiveOnes(nums = [1,0,1,1,0]))
    print(obj.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1,1,1,0,1]))

    #print(obj.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]))

# [0, 1, 4, 8, 10]

#

# Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

# Example 1:

# Input: nums = [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
 

# Follow up: What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


