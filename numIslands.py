class Solution:
    def numIslands(self, grid):
        self.m, self.n = len(grid), len(grid[0])

        visited = set()

        res = 0

        for swi in range(self.m):
            for swj in range(self.n):
                if grid[swi][swj] == '1' and (swi, swj) not in visited:
                    self.dfs((swi, swj), visited)
                    res = res + 1
        
        return res

    def dfs(self, v, visited):
        if v in visited: return
        visited.add(v)
        i,j = v
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj] == "1":
                dfs((i+di,j+dj), visited)
        m, n = len(grid), len(grid[0])



        if v in visited:
            return 

        visited.add(v)
        swi, swj = v

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= (swi + di) < self.m and 0 <= (swj + dj) < self.n and grid[swi + di][swj + dj] == '1':
                self.dfs((swi+di, swj+dj), visited)
        

if __name__ == "__main__":
    obj = Solution()

    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

    print(obj.numIslands(grid))

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