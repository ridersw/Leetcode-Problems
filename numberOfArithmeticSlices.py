


class Solution:
    def numberOfArithmeticSlices(self, nums):
        le = len(nums)
        l = [0] * le
        
        for swi in range(2, le):
            if nums[swi] - nums[swi-1] == nums[swi-1] - nums[swi-2]:
                l[swi] = 1 + l[swi-1]
                
        print(l)
        return sum(l)


if __name__ == "__main__":
    obj = Solution()
    # print(obj.numberOfArithmeticSlices(nums = [1,2,3,4]))
    # print(obj.numberOfArithmeticSlices(nums = [1]))
    print(obj.numberOfArithmeticSlices(nums=[1,2,3,8,9,10]))