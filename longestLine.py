from tkinter import HORIZONTAL, VERTICAL


class Solution:
    def longestLine(self, mat):
        n=len(mat)
        m=len(mat[0])
        dp=[[[0,0,0,0] for i in range(m)] for j in range(n)]
        maxx=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    continue
                if i-1 >= 0 and j-1 >= 0:
                    dp[i][j][3]=1+dp[i-1][j-1][3]
                else:
                    dp[i][j][3]=1
                if i-1 >= 0:
                    dp[i][j][0]=1+dp[i-1][j][0]
                else:
                    dp[i][j][0]=1
                if j-1 >=0:
                    dp[i][j][1]=1+dp[i][j-1][1]
                else:
                    dp[i][j][1]=1
                if i-1 >= 0 and j+1 < m:
                    dp[i][j][2]=1+dp[i-1][j+1][2]
                else:
                    dp[i][j][2]=1
                maxx1=max(dp[i][j])
                maxx=max(maxx,maxx1)
        return maxx
            

if __name__ == "__main__":
    obj = Solution()

    mat =   [[0,1,1,0],
            [0,1,1,0],
            [0,0,0,1]]

    print(obj.longestLine(mat))

# Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

# The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

# Example 1:


# Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
# Output: 3
# Example 2:


# Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
# Output: 4
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.