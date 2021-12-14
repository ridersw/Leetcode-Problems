class Solution:
    def canPartition(self, nums):
        if sum(nums)/2 != int(sum(nums)/2):
            return False

        half = int(sum(nums)/2)

        def canSum(nums, target, memo = {}):
            if target in memo:
                return memo[target]

            if target == 0:
                return True

            if target < 0:
                return False

            for swi in range(len(nums)):
                newTarget = target - nums[swi]
                remain = canSum(nums[swi+1:], newTarget)

                if remain == True:
                    memo[target] = True
                    return memo[target]

            memo[target] = False
            return memo[target]

        return canSum(nums, half)

    def canPartitionNumbers(self, nums):
        if sum(nums)/2 != int(sum(nums)/2):
            return False

        half = int(sum(nums)/2)

        def canSum(nums, target, memo = {}):
            if target in memo:
                return memo[target]

            if target == 0:
                return []

            if target < 0:
                return None

            for swi in range(len(nums)):
                arr = []
                newTarget = target - nums[swi]
                remain = canSum(nums[swi+1:], newTarget, memo)

                if remain != None:
                    remain.append(nums[swi])
                    memo[target] = remain
                    return memo[target]

            memo[target] = None
            return None

        return canSum(nums, half)

if __name__ == "__main__":
    obj = Solution()

    nums = [1,5,11,5]
    #nums = [1,2,3,5]
    #nums = [10,2,11,1]

    print(obj.canPartition(nums))

# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:

# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100