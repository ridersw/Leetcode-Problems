class Solution:
    def maxDistToClosest(self, seats):
        print(f'seats: {seats}')
        maxDistance = 0

        backwardMemo = {}
        forwardMemo = {}

        for swi in range(len(seats)):
            if seats[swi] != 1:
                print(f'Checking for Element at Index: {swi}')
                if 1 in seats[:swi]:
                    backwardDistance = 0
                    for swj in range(swi, 0, -1):
                        if swj in backwardMemo:
                            backwardDistance += backwardMemo[swj]
                            break

                        if seats[swj] == 0:
                            backwardDistance += 1
                        else:
                            break
                else:
                    backwardDistance = float('inf')

                backwardMemo[swi] = backwardDistance

                print(f'backwardDistance: {backwardDistance}')

                if 1 in seats[swi+1:]:
                    forwardDistance = 0
                    for swk in range(swi, len(seats)):
                        if swk in forwardMemo:
                            backwardDistance += forwardMemo[swk]
                            break

                        if seats[swk] == 0:
                            forwardDistance += 1
                        else:
                            break

                    print(f'forwardDistance: {forwardDistance}')
                else:
                    forwardDistance = float('inf')

                forwardMemo[swi] = forwardDistance

                maxDistance = max(maxDistance, min(forwardDistance, backwardDistance))
                print(f'maxDistance: {maxDistance}')
    
        return maxDistance

                

if __name__ == "__main__":
    obj = Solution()

    seats = [1,0,0,0,1,0,1]
    seats = [1,0,0,0]
    #seats = [0,1]
    #seats = [0,1,0,1,0]

    print(obj.maxDistToClosest(seats))

# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

# There is at least one empty seat, and at least one person sitting.

# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

# Return that maximum distance to the closest person.

 

# Example 1:


# Input: seats = [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:

# Input: seats = [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Example 3:

# Input: seats = [0,1]
# Output: 1
 

# Constraints:

# 2 <= seats.length <= 2 * 104
# seats[i] is 0 or 1.
# At least one seat is empty.
# At least one seat is occupied.