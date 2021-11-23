class Solution:
    def maxSubArray(self, nums):
        maxSoFar = nums[0]
        maxEndHere = 0

        for swi in range(len(nums)):
            maxEndHere += nums[swi]

            if maxEndHere > maxSoFar:
                maxSoFar = maxEndHere
            
            if maxEndHere < 0:
                maxEndHere = 0

        return maxSoFar

        


if __name__ == "__main__":
    obj = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]

    print(obj.maxSubArray(nums))