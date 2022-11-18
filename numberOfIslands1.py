class Solution:
    def numberOfIslands(self, grid):
        result = 0
        self.grid = grid

        if len(self.grid) == 1:
            swi = 0
            while swi < len(self.grid[0]):
                print(f'grid[swi]: {self.grid[0][0]} swi: {swi}')
                if self.grid[0][swi] == '1':
                    result += 1
                    while swi < len(self.grid[0]) and self.grid[0][swi] == '1':
                        swi += 1
                else:
                    swi += 1

            return result


        for swi in range(len(grid)):
            for swj in range(len(grid[0])):
                # print(f'In numberOfIslands Function: grid[{swi}][{swj}] grid: {self.grid} current_islands: {result}')
                if grid[swi][swj] != None and grid[swi][swj] == '1':
                    result += 1
                    self.findLand([swi, swj])
                else:
                    continue

        return result

    def findLand(self, starting_point):
        # print(f'=========================================================')
        # print(f'In findIsland Function with Parameters: {starting_point}')
        # print(f'=========================================================')
        if starting_point[0] < 0 or starting_point[0] > len(self.grid[0]) or starting_point[1] < 0 or starting_point[1] > len(self.grid):
            return
        
        for swi in range(starting_point[0], len(self.grid)):
            for swj in range(starting_point[1], len(self.grid[0])):
                # print(f'swi: {swi} swj: {swj} grid[swi][swj]: {self.grid[swi][swj]}')
                if self.grid[swi][swj] == '1':
                    self.grid[swi][swj] = "#"
                    self.findLand([swi+1, swj])
                    self.findLand([swi-1, swj])
                    self.findLand([swi, swj+1])
                    self.findLand([swi, swj-1])
                else:
                    return 



if __name__ == "__main__":
    obj = Solution()

    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

    grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

    grid = [["1","0","1","1","0","1","1"]]
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