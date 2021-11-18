class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return max(nums)
        
        dp = [0] * len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for swi in range(2, len(nums)):
            dp[swi] = max(dp[swi-2] + nums[swi], dp[swi-1])
            
        return dp[-1]
        
