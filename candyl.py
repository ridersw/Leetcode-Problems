class Solution:
    def candy(self, ratings: List[int]) -> int:

        result = [1] * len(ratings)

        for swi in range(1, len(ratings)):
            if ratings[swi] > ratings[swi-1]:
                result[swi] = result[swi-1] + 1
                
        for swi in range(len(ratings)-2, -1, -1):
            if ratings[swi] > ratings[swi+1]:
                result[swi] = max(result[swi], result[swi+1]+1)
        
        return sum(result)
        




if __name__ == "__main__":
    obj = Solution()
    # print(obj.candy(ratings = [1,0,2]) == 5)
    # print(obj.candy(ratings = [1,3,2]) == 4)
    # print(obj.candy(ratings = [1, 3, 4, 5, 2]) == 11)
    print(obj.candy(ratings = [5, 4, 3, 2, 1]) == 15)
    # print(obj.candy(ratings = [1,3,2,2,1]) == )

# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.

 

# Example 1:

# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# Example 2:

# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
 

# Constraints:

# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104