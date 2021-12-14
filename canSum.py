class Solution:
    def canSum(self, nums, target):
        
        if target == 0:
            return True

        if target < 0:
            return False

        for swi in range(len(nums)):
            newTarget = target - nums[swi]
            remain = self.canSum(nums[swi+1:], newTarget)

            if remain == True:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()

    nums = [10,11, 1, 2]
    nums = [1,5,11,5]

    target = 11

    print(obj.canSum(nums, target))