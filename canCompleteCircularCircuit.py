class Solution:
    def canCompleteCircuit(self, gas, cost):
    #     startingStations = []

    #     for swi in range(len(gas)):
    #         if gas[swi] > cost[swi]:
    #             startingStations.append(swi)

    #     ans = -1

    #     if len(startingStations) == 0:
    #         return -1

    #     print(f'Found Starting Stations: {startingStations}')

    #     for startIndex in startingStations:
    #         print(f'=======================================')
    #         print(f'From Station: {startIndex}')
    #         print(f'=======================================')
    #         ans = self.helper(startIndex, gas, cost)
    #         if ans > 0:
    #             return startIndex

    #     return ans


    # def helper(self, startIndex, gas, cost):
    #     fuel = 0
    #     for swi in range(startIndex, len(gas)):
    #         fuel += gas[swi] - cost[swi]
    #         print(f'Line 31) Traveling to {swi} from {startIndex} Fuel: {fuel}')

    #         if fuel <= 0:
    #             return -1

    #     if startIndex > 0:
    #         for swi in range(0, startIndex+1):
    #             fuel += gas[swi] - cost[swi]
    #             print(f'Line 39) Traveling to {swi} from {startIndex} Fuel: {fuel}')

    #             if swi == startIndex:
    #                 return startIndex

    #             if fuel <= 0:
    #                 return -1

    #         if fuel <= 0:
    #             return -1

    #     return startIndex
        # n = len(gas)
        
        # total_tank = curr_tank = 0
        # starting_station = 0
        
        # for swi in range(n):
        #     total_tank += gas[swi] - cost[swi]
        #     curr_tank += gas[swi] - cost[swi]
            
        #     if curr_tank < 0:
        #         starting_station = swi+1
        #         curr_tank = 0
                
        # return starting_station if total_tank >= 0 else -1

        diff = []

        for swi in range(len(gas)):
            diff.append(gas[swi] - cost[swi])

        print(f'diff: {diff}')

        startingIndex = []

        for swi in range(len(diff)):
            if diff[swi] >= 0:
                startingIndex.append(swi)


        for swi in startingIndex:
            # print(f'Checking for StartingIndex: {swi}')
            sum = 0
            for swj in range(swi, len(diff)):
                sum += diff[swj]
                # print(f'Line 85) Sum: {sum}')
                if sum < 0:
                    return -1

            # print(f'Till Last: {sum}')

            for swj in range(0, swi):
                # print(f'Adding {diff[swj]} to {sum}')
                sum += diff[swj]
                # print(f'Line 94) Sum: {sum}')
                if sum < 0:
                    return -1

            # print(f'From first to startIndex: {sum}')

            if sum >= 0:
                return swi

        return -1
        

if __name__ == "__main__":
    obj = Solution()
    # print(obj.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
    # print(obj.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
    print(obj.canCompleteCircuit(gas = [1,2,3,4,3,2,4,1,5,3,2,4], cost = [1,1,1,3,2,4,3,6,7,4,3,1]))
# 

    
# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

# Example 1:

# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
# Therefore, return 3 as the starting index.
# Example 2:

# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
# Therefore, you can't travel around the circuit once no matter where you start.
 

# Constraints:

# n == gas.length == cost.length
# 1 <= n <= 105
# 0 <= gas[i], cost[i] <= 104