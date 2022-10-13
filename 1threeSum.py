class Solution:
    def threeSum(self, nums):
        res = set()

        n, p, z = [], [], []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)

        if z:
            for num in P:
                if -1 * num in N:
                    res.add(-1*num, 0, num)

        if len(z) >= 3:
            res.add((0,0,0))

        for swi in range(len(n)):
            for swj in range(swi+1, len(n)):
                target = -1 * (n[swi] + n[swj])
                if target in P:
                    res.add(tuple(sorted(n[swi], n[swj], target)))

        for swi in range(len(p)):
            for swj in range(swi+1, len(p)):
                target = -1 * (p[swi] + p[swj])
                if target in N:
                    res.add(tuple(sorted(p[swi], p[swj], target)))
        
        return res

         

if __name__ == "__main__":
    obj = Solution()
    print(obj.threeSum(nums = [-1,0,1,2,-1,-4]))

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105