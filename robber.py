class Solution:
    def robber(self, houses):
        if len(houses) < 3:
            return max(houses)

        dp = [0] * len(houses)

        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for swi in range(2, len(houses)):
            dp[swi] = max(dp[swi-2] + houses[swi], dp[swi-1])

        return max(dp[-1], dp[-2])

if __name__ == "__main__":
    obj = Solution()

    houses = [1,2,3,1]

    print(obj.robber(houses))
