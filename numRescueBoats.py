class Solution:
    def numRescueBoats(self, people, limit):

        people = sorted(people)

        start = count = 0
        end = len(people)-1

        while start <= end:
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
            count += 1
        return count

if __name__ == "__main__":
    obj = Solution()

    print(obj.numRescueBoats(people = [1,2], limit = 3))
    print(obj.numRescueBoats(people = [1,2,2,3], limit = 3))
    print(obj.numRescueBoats(people = [3,5,3,4], limit = 5))

    #5 1 4 2
    #6
    # 
    # 5 4 2 1  

# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

 

# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
 

# Constraints:

# 1 <= people.length <= 5 * 104
# 1 <= people[i] <= limit <= 3 * 104