class Solution:
    def twoSum(self, nums, target):
        
        for swi in range(len(nums)-1):
            for swj in range(swi+1, len(nums)):
                if nums[swi] + nums[swj] == target:
                    return [swi, swj]



if __name__ == "__main__":
    obj = Solution()

    nums = [2,7,11,15]
    target = 9

    print(obj.twoSum(nums, target))