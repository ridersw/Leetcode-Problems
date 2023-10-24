class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = set()
        self.grid = grid
        self.m = len(self.grid)
        self.n = len(self.grid[0])
        count = 0
        
        for swi in range(self.m):
            for swj in range(self.n):
                if grid[swi][swj] == '1' and (swi, swj) not in self.visited:
                    self.travel((swi, swj))
                    count += 1
                    
        return count
    
    def travel(self, v):
        if v in self.visited:
            return
        
        self.visited.add(v)
        
        swi, swj = v
        
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= (swi + di) < self.m and 0 <= (swj + dj) < self.n and self.grid[swi+di][swj+dj] == "1":
                self.travel((swi+di, swj + dj))

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