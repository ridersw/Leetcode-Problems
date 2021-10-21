class Solution:
    def tribonacci(self, n, memo = {}):
        
        if n == 0:
            return 0

        if n <= 2:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return memo[n]


if __name__ == "__main__":
    obj = Solution()

    print(obj.tribonacci(29))