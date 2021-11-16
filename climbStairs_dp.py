class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n < 0:
            return 0
        
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]

if __name__ == "__main__":
    obj = Solution()
    print(obj.climbStairs(2))