from functools import cache


class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        @cache
        def dfs(swi, swj):
            if swi == n          : return 0 

            # if swi < 0 or swj == n:
            if swj < 0 or swj == n:    
                
                return float('inf') 
                

            return matrix[swi][swj] + min(dfs(swi+1,swj-1), dfs(swi+1,swj), dfs(swi+1,swj+1))

        return min(dfs(0,j) for j in range(n))   

    
if __name__ == "__main__":
    obj = Solution()
    print(obj.minFallingPathSum(matrix = [[2,1,3],[6,5,4],[7,8,9]]))
    print(obj.minFallingPathSum(matrix = [[-19,57],[-40,-5]]))
    print(obj.minFallingPathSum(matrix = [[-48]]))