class Solution:
    def maximalSquare(self, matrix):

        # def helper(row, col):
        #     if row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] == '0':
        #         return 0
        #     return 1 + min(helper(row+1, col), helper(row, col+1), helper(row+1, col+1))

        # res = 0
        # for r in range(len(matrix)):
        #     for c in range(len(matrix[0])):
        #         res = max(res, helper(r, c))

        # return res**2

        if len(matrix) == 0:
            return 0

        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0 for swi in range(cols+1)] for swi in range(rows+1)]

        for r in range(rows, -1, -1):
            for c in range(cols, -1, -1):
                if r >= rows or c >= cols or matrix[r][c] == '0':
                    continue
                else:
                    dp[r][c] = 1 + min(dp[r][c+1],dp[r+1][c],dp[r+1][c+1])
                    res = max(res, dp[r][c])

        return res ** 2

   

if __name__ == "__main__":
    obj = Solution()

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["0","1"],["1","0"]]
    matrix = [["1"]]

    print(obj.maximalSquare(matrix))

# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.