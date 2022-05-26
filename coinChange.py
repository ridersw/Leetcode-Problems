from curses.ascii import SP


class Solution:
    def coinChange(self, coins, amount):
        # coins.sort()
        # pointer = len(coins)-1
        # coinCount = 0

        # while amount > 0 and pointer >= 0:
        #     print(f'amount: {amount} and coins[pointer]:{coins[pointer]}')
        #     if coins[pointer] <= amount:
        #         tempAmount = amount
        #         amount = amount % coins[pointer]
        #         coinCount = coinCount + ((tempAmount-amount) // coins[pointer])
                
        #     pointer = pointer - 1

        # if amount == 0:
        #     return coinCount
        # return -1

        def newCoinChange(swi, coins, amount):
            if amount == 0:
                return 0
            if swi == len(coins) or amount < 0:
                return float('INF')
            return min(newCoinChange(swi, coins, amount-coins[swi]) + 1, newCoinChange(swi+1, coins, amount))

        return newCoinChange(0, coins, amount)



if __name__ == "__main__":  

    obj = Solution()

    coins = [1,2,5]
    amount = 11

    coins = [2]
    amount = 3

    coins = [1]
    amount = 0

    coins = [186,419,83,408]
    amount = 6249

    print(obj.coinChange(coins, amount))

    