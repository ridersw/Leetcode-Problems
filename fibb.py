class Solution:
    def fibb(self, n, memo = {}):
        if n == 0:
            return 0

        if n <= 2:
            return 1

        if n in memo:
            return memo[n]

        memo[n] = self.fibb(n-1) + self.fibb(n-2)
        return memo[n]

if __name__ == "__main__":
    obj = Solution()

    print(obj.fibb(4))