from tabnanny import check


class Solution:
    def minDominoRotations(self, tops, bottoms):

        def check(x):
            rotations_a, rotations_b = 0, 0
            
            for swi in range(n):
                if tops[swi] != x and bottoms[swi] != x:
                    return -1
                
                elif tops[swi] != x:
                    rotations_a += 1
                    
                elif bottoms[swi] != x:
                    rotations_b += 1
                    
            return min(rotations_a, rotations_b)
            
        n = len(tops)
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])


if __name__ == "__main__":
    obj = Solution()

    print(obj.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
    #print(obj.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
    #print(obj.minDominoRotations(tops = [1,2,2,1,2,1,2,1,2], bottoms= [1,2,1,1,1,1,2,1,2]))
    #print(obj.minDominoRotations(tops = [2,1,1,3,2,1,2,2,1], bottoms = [3,2,3,1,3,2,3,3,2]))

# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
 
# Constraints:

# 2 <= tops.length <= 2 * 104
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6