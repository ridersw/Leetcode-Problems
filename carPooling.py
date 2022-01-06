class Solution:
    def carPooling(self, trips, capacity):
        # originalCapacity = capacity
        # pickup = []
        # dropoff = []
        # numberOfPeople = []

        # for record in trips:
        #     numberOfPeople.append(record[0])
        #     pickup.append(record[1])
        #     dropoff.append(record[2])

        # print(f'numberOfPeople: {numberOfPeople}')
        # print(f'pickup: {pickup}')
        # print(f'dropoff: {dropoff}')

        # end = max(max(pickup), max(dropoff))
        # start = min(min(pickup), min(dropoff))
        # print(f'start: {start} and end: {end}')


        # for swi in range(start, end+1):
        #     print(f'At location: {swi}')

        #     if swi in dropoff:
        #         print(f'{swi} is Dropoff point')
        #         temp = dropoff.index(swi)
        #         print(f'Current Capacity: {capacity}, updated Capacity after dropping off: {capacity + numberOfPeople[temp]}')
        #         capacity += numberOfPeople[temp]

        #     if swi in pickup:
        #         print(f'{swi} is Pickup point')
        #         temp = pickup.index(swi)
        #         if capacity - numberOfPeople[temp] >= 0:
        #             print(f'Capacity Available: {capacity}, updated Capacity after picking up: {capacity - numberOfPeople[temp]}')
        #             capacity -= numberOfPeople[temp]
        #         else:
        #             print(f'Capacity Exceeded')
        #             return False

        # return True 

        lst = []

        for numberOfPeople, start, end in trips:
            lst.append((start, numberOfPeople))
            lst.append((end, -numberOfPeople))

        lst.sort()

        print(f'lst: {lst}')

        passengers = 0

        for loc in lst:
            print()
            passengers += loc[1]
            if passengers > capacity:
                return False
        return True


if __name__ == "__main__":
    obj = Solution()

    trips = [[2,1,5],[3,3,7]]
    capacity = 4

    # trips = [[2,1,5],[3,3,7]]
    # capacity = 5

    # trips = [[2,1,5],[3,5,7]]
    # capacity = 3

    # trips = [[3,6,9],[10,2,3],[1,6,8],[2,1,6],[9,3,9]]
    # capacity = 12

    #         capacity
    # 1 ->    12 - 2 = 10
    # 2 ->    10 - 10 = 0
    # 3 ->    
    # 4 -> 
    # 5 -> 
    # 6 -> 
    # 7 -> 
    # 8 -> 
    # 9 -> 

    print(obj.carPooling(trips, capacity))

# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true