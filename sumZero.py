class Solution:
    def sumZero(self, n):
        
        if n % 2 == 0:
            arr = []
        else:
            arr = [0]
            n -= 1

        for swi in range(3, (n//2)+3):
            arr.append(swi)
            arr.append(-swi)

        return arr


if __name__ == "__main__":
    obj = Solution()
    
    n = 5

    print(obj.sumZero(n))

# Given an integer n, return any array containing n unique integers such that they add up to 0.

 

# Example 1:

# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: n = 3
# Output: [-1,0,1]
# Example 3:

# Input: n = 1
# Output: [0]