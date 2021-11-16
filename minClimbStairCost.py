class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        tempArray = cost[:2]
        
        for swi in range(2, len(cost)):
            tempArray.append(min(tempArray[swi-1] + cost[swi], tempArray[swi-2] + cost[swi]))
            
        return min(tempArray[-1], tempArray[-2])

if __name__ == "__main__":
    obj= Solution()
    print(obj.minCostClimbingStairs(cost = [10,15,20]))