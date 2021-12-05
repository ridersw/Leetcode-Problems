class Solution:
    def maxProfit(self, prices):
        # n = len(prices)

        # currentProfit = maxSoFar = 0
        # print(f'prices: {prices}')

        # for swi in range(1, n):
        #     print(f'fot loop {swi}: currentProfit: {currentProfit} and maxSoFar: {maxSoFar} prices[swi]: {prices[swi]} and prices[swi-1]: {prices[swi-1]}')
        #     currentProfit = max(currentProfit + prices[swi] - prices[swi-1], 0)
        #     maxSoFar = max(currentProfit, maxSoFar)

        # return maxSoFar


        maxPro = 0

        for swi in range(len(prices)-1):
            print(f'maxPro: {maxPro} = max(prices[swi]: {prices[swi]} - max(prices[swi+1:]): {max(prices[swi+1:])}, prices[swi] - max(prices[swi+1:]): {prices[swi] - max(prices[swi+1:])} , maxPro: {maxPro})')
            maxPro = max(max(prices[swi+1:]) - prices[swi], maxPro)

        return maxPro



if __name__ == "__main__":
    obj = Solution()

    prices = [7,1,5,3,6,4]

    print(obj.maxProfit(prices))