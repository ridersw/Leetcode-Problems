class Solution:
    def maxProfit(self, prices):
        # if not prices:
        #     return 0

        # maxProfit = 0
        # minPurchase = prices[0]

        # for swi in range(1, len(prices)):
        #     maxProfit = max(maxProfit, prices[swi] - minPurchase)
        #     minPurchase = min(minPurchase, prices[swi])

        # return maxProfit

        max_profit = 0
        min_purchase = prices[0]
        # for swi in range(len(prices)-1):
        #     for swj in range(swi+1, len(prices)):
        #         max_profit = max(max_profit, prices[swj] - prices[swi])

        for swi in range(len(prices)):
            max_profit = max(max_profit, prices[swi] - min_purchase)
            min_purchase = min(min_purchase, prices[swi])

        return max_profit


if __name__ == "__main__":
    obj = Solution()

    print(obj.maxProfit(prices = [7,1,5,3,6,4]))

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104