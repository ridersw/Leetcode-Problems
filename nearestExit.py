import math
import collections

class Solution:
    def nearestExit(self, maze, entrance) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"

        queue = collections.deque()
        queue.append([start_row, start_col, 0])

        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()

            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])

        return -1



if __name__ == "__main__":
    obj = Solution()

    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]

    maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    entrance = [1,0]

    print(obj.nearestExit(maze, entrance))

# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

# Example 1:


# Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
# Output: 1
# Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
# Initially, you are at the entrance cell [1,2].
# - You can reach [1,0] by moving 2 steps left.
# - You can reach [0,2] by moving 1 step up.
# It is impossible to reach [2,3] from the entrance.
# Thus, the nearest exit is [0,2], which is 1 step away.
# Example 2:


# Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
# Output: 2
# Explanation: There is 1 exit in this maze at [1,2].
# [1,0] does not count as an exit since it is the entrance cell.
# Initially, you are at the entrance cell [1,0].
# - You can reach [1,2] by moving 2 steps right.
# Thus, the nearest exit is [1,2], which is 2 steps away.
# Example 3:


# Input: maze = [[".","+"]], entrance = [0,0]
# Output: -1
# Explanation: There are no exits in this maze.
 

# Constraints:

# maze.length == m
# maze[i].length == n
# 1 <= m, n <= 100
# maze[i][j] is either '.' or '+'.
# entrance.length == 2
# 0 <= entrancerow < m
# 0 <= entrancecol < n
# entrance will always be an empty cell.