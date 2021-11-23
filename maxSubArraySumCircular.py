class Solution:
    def maxSubArraySumCircular(self, nums):
        max_so_far = min_so_far = min_ending_here = max_ending_here = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)    
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        if min_so_far == sum(nums):
            return max_so_far
        else:
            return max(max_so_far,sum(nums)-min_so_far)

if __name__ == "__main__":
    obj = Solution()

    nums = [1,-2,3,-2]
    nums = [5,-3,5]
    nums = [-2,-3,-1]


    print(obj.maxSubArraySumCircular(nums))