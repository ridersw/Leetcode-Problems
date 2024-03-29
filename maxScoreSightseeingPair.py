class Solution:
    def maxScoreSightseeingPair(self, values):    
        maxVal = 0
        cur = 0            
        for i in range(1, len(values)):
            cur = max(cur, values[i-1]+i-1)
            maxVal = max(maxVal, cur+values[i]-i)
        return maxVal


if __name__ == "__main__":
    obj = Solution()
    values = [8,1,5,2,6]
    values = [1,2]
    print(obj.maxScoreSightseeingPair(values))

# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

 

# Example 1:

# Input: values = [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
# Example 2:

# Input: values = [1,2]
# Output: 2

