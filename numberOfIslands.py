from collections import deque


class Solution:
    def numberOfIslands(self, grid):
        self.visited = set()

        self.m = len(grid)
        self.n = len(grid[0])

        self.grid = grid

        result = 0

        for swi in range(self.m):
            for swj in range(self.n):
                if self.grid[swi][swj] == '1' and (swi, swj) not in self.visited:
                    self.bfs(swi, swj)
                    result += 1

        return result


    def isValid(self, row, col):
        if row < 0 or col < 0 or row >= len(self.grid) or col >= len(self.grid[0]) or self.grid[row][col] != '1' or (row, col) in self.visited:
            return False
        return True

    def bfs(self, row, col):
        queue = deque()
        queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            if not self.isValid(row, col):
                continue
            self.visited.add((row, col))
            queue.append((row, col+1))
            queue.append((row, col-1))
            queue.append((row-1, col))
            queue.append((row+1, col))

        

if __name__ == "__main__":
    obj = Solution()

    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    print(obj.numberOfIslands(grid))

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.