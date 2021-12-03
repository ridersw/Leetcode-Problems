class Solution:
    def maxProfit(self, prices):
        dp = {}

        def dfs(swi, buying):
            if swi >= len(prices):
                return 0

            if (swi, buying) in dp:
                return dp[(swi, buying)]

            if buying:
                buy = dfs(swi+1, not buying) - prices[swi]
                cooldown = dfs(swi+1, buying)
                dp[(swi, buying)] = max(buy, cooldown)        
            else:
                sell = dfs(swi+2, not buying) + prices[swi]
                cooldown = dfs(swi+1, buying)
                dp[(swi, buying)] = max(sell, cooldown)       
            return dp[(swi, buying)]

        return dfs(0, True)


if __name__ == "__main__":
    obj = Solution()

    prices = [1,2,3,0,2]

    print(obj.maxProfit(prices))

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# Example 2:

# Input: prices = [1]
# Output: 0