class Solution:
    def combinationSum4(self, nums, target, combo = []):

        # if target == 0:
        #     return [[]]

        # result = []

        # for number in nums:
        #     remainder = target - number
        #     remainderResult = self.combinationSum4(nums, remainder)

        #     if remainderResult != None:
        #         remainderResult.append(number)
        #         return remainderResult

        # return None
        dp = [0 for swi in range(target+1)]

        print(f'dp: {dp}')

        dp[0] = 1

        print(f'dp: {dp}')

        for comb_sum in range(target+1):
            print(f'Outer Loop dp: {dp}')
            for num in nums:
                dp[comb_sum] += dp[comb_sum-num]
                print(f'Inner Loop dp: {dp}')

        return dp[target]


if __name__ == "__main__":
    obj = Solution()

    nums = [1,2,3]
    target = 4

    print(obj.combinationSum4(nums, target))

# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# Example 2:

# Input: nums = [9], target = 3
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
 

# Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
        