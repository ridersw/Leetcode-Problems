class Solution:
    def sortColors(self, nums):
        
        for swi in range(len(nums)):
            pos = swi
            for swj in range(swi+1, len(nums)):
                if nums[swj] < nums[pos]:
                    pos = swj

            nums[swi], nums[pos] = nums[pos], nums[swi]

        return nums


if __name__ == "__main__":
    obj = Solution()
    print(obj.sortColors(nums = [2,0,2,1,1,0]))