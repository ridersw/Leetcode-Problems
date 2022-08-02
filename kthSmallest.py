class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(mid):
            cnt = 0
            for r in range(N):
                x = bisect_right(matrix[r], mid)
                cnt += x
            return cnt
                
        
        while left< right:
            middle = (left + right) // 2
            if less_k(middle) < k:
                left = middle + 1
            else:
                right = middle
                
        return left
        
