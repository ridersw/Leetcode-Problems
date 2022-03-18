class Solution:
    def findDisappearedNumbers(self, nums):
        nums.sort()
        length = len(nums)
        nums = list(set(nums))
        res = []

        print(f'nums: {nums}')
        pointer = 0
        swi = 1
        nums.append(-1)

        while swi < length+1:
            print(f'checking for {swi} and {nums[pointer]}')
            if swi == nums[pointer]:
                print(f'Found: {swi}')
                swi += 1
                pointer += 1
            else:
                #if nums[pointer] > swi:
                res.append(swi)
                swi += 1
                #else:
        return res



if __name__ == "__main__":
    obj = Solution()

    #print(obj.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
    print(obj.findDisappearedNumbers(nums = [1,1]))

# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:

# Input: nums = [1,1]
# Output: [2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 105
# 1 <= nums[i] <= n
 

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.