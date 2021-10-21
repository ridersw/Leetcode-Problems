class Solution:
    def minCostClimbingStairs(self, cost):

        tempCost = cost[:2]

        cost.append(0)

        for swi in range(2, len(cost)):
            tempCost.append(min(cost[swi] + tempCost[swi-1], cost[swi] + tempCost[swi-2]))

        return min(tempCost[-1], tempCost[-2])


if __name__ == "__main__":
    obj = Solution()

    cost = [10,15,20]

    print(obj.minCostClimbingStairs(cost))