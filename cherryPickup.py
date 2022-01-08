class Solution:
    def cherryPickup(self, grid):
        robot1 = grid[0][0]
        robot2 = 0
        swi1 = 0
        swj1 = 0
        swi2 = 0
        swj2 = len(grid)-1

        while swi1 < len(grid) - 1 and swj1 < len(grid[0]) and swj1 >= 0 and swj1 < len(grid[0]) - 1 and swj2 < len(grid[0]) and swj2 >= 0:
            #for robot 1
            print(f'robot1: {robot1} and its location {swi1} and {swj1} len(grid): {len(grid)} and len(grid[0]): {len(grid[0])}' )

            #when robot is in leftmost cornor
            if swj1 == 0:
                # print('when robot is in leftmost cornor')
                if grid[swi1+1][swj1] > grid[swi1+1][swj1+1]:
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    robot1 += grid[swi1+1][swj1+1]
                    grid[swi1+1][swj1+1] = 0
                    if swi1 + 1 <len(grid) and swj1 + 1 < len(grid[0]):
                        swi1 += 1
                        swj1 += 1

            #when robot is in rightmost cornor
            elif swj1 == len(grid[0])-1:
                # print('when robot is in rightmost cornor')
                if grid[swi1+1][swj1] > grid[swi1+1][swj1-1]:
                    print('if loop')
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    print('else loop')
                    robot1 += grid[swi1+1][swj1-1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid) and swj1 - 1 >= 0:
                        swi1 += 1
                        swj1 -= 1
                    

            #when robot is in middle
            else:
                # print('when robot is in middle')
                # print(f'grid[swi1+1][swj1-1]: {grid[swi1+1][swj1-1]}')
                # print(f'grid[swi1+1][swj1]: {grid[swi1+1][swj1]}')
                # print(f'grid[swi1+1][swj1+1]: {grid[swi1+1][swj1+1]}')
                if grid[swi1+1][swj1-1] > grid[swi1+1][swj1] and grid[swi1+1][swj1-1] > grid[swi1+1][swj1+1]:
                    # print('condition 1')
                    robot1 += grid[swi1+1][swj1-1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid) and swj1 - 1 > 0:  
                        swi1 += 1
                        swj1 -= 1
                elif grid[swi1+1][swj1] > grid[swi1+1][swj1-1] and grid[swi1+1][swj1] > grid[swi1+1][swj1+1]:
                    # print('condition 2')
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    # print('condition 3')
                    robot1 += grid[swi1+1][swj1+1]
                    grid[swi1+1][swj1+1] = 0
                    if swi1 + 1 <len(grid) and swj1 + 1 < len(grid[0]):
                        swi1 += 1
                        swj1 += 1

            # for robot 2

            print(f'robot2: {robot1} and its location {swi2} and {swj2} len(grid): {len(grid)} and len(grid[0]): {len(grid[0])}' )


            #when robot is in leftmost cornor
            if swj1 == 0:
                # print('when robot is in leftmost cornor')
                if grid[swi1+1][swj1] > grid[swi1+1][swj1+1]:
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    robot1 += grid[swi1+1][swj1+1]
                    grid[swi1+1][swj1+1] = 0
                    if swi1 + 1 <len(grid) and swj1 + 1 < len(grid[0]):
                        swi1 += 1
                        swj1 += 1

            #when robot is in rightmost cornor
            elif swj1 == len(grid[0])-1:
                # print('when robot is in rightmost cornor')
                if grid[swi1+1][swj1] > grid[swi1+1][swj1-1]:
                    print('if loop')
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    print('else loop')
                    robot1 += grid[swi1+1][swj1-1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid) and swj1 - 1 >= 0:
                        swi1 += 1
                        swj1 -= 1
                    

            #when robot is in middle
            else:
                # print('when robot is in middle')
                # print(f'grid[swi1+1][swj1-1]: {grid[swi1+1][swj1-1]}')
                # print(f'grid[swi1+1][swj1]: {grid[swi1+1][swj1]}')
                # print(f'grid[swi1+1][swj1+1]: {grid[swi1+1][swj1+1]}')
                if grid[swi1+1][swj1-1] > grid[swi1+1][swj1] and grid[swi1+1][swj1-1] > grid[swi1+1][swj1+1]:
                    # print('condition 1')
                    robot1 += grid[swi1+1][swj1-1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid) and swj1 - 1 > 0:  
                        swi1 += 1
                        swj1 -= 1
                elif grid[swi1+1][swj1] > grid[swi1+1][swj1-1] and grid[swi1+1][swj1] > grid[swi1+1][swj1+1]:
                    # print('condition 2')
                    robot1 += grid[swi1+1][swj1]
                    grid[swi1+1][swj1-1] = 0
                    if swi1 + 1 <len(grid):
                        swi1 += 1
                else:
                    # print('condition 3')
                    robot1 += grid[swi1+1][swj1+1]
                    grid[swi1+1][swj1+1] = 0
                    if swi1 + 1 <len(grid) and swj1 + 1 < len(grid[0]):
                        swi1 += 1
                        swj1 += 1

        return robot1 + robot2



if __name__ == "__main__":
    obj = Solution()

    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]

    print(obj.cherryPickup(grid))