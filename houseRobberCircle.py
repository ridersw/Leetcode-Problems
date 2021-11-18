class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        
        def checkAmount(newNums):
            dp = [0] * len(newNums)
            dp[0] = newNums[0]
            dp[1] = max(newNums[1], newNums[0])
            
            for swi in range(2, len(newNums)):
                dp[swi] = max(dp[swi-2] + newNums[swi], dp[swi-1])
        
            return max(dp)
        
        firstSelected = nums[:len(nums)-1]
        lastSelected = nums[1:]
        
        first = checkAmount(firstSelected)
        last = checkAmount(lastSelected)
        
        return max(first, last)
        
