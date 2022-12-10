# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        all_sums = []
        
        def sumdfs(node):
            if node is None:
                return 0
            
            left_sum = sumdfs(node.left)
            right_sum = sumdfs(node.right)
            # print(f'On Node: {node.val} left_sum: {left_sum} and right_sum: {right_sum} total_sum: {node.val + left_sum + right_sum}')
            total_sum = node.val + left_sum + right_sum
            all_sums.append(total_sum)
            return total_sum
            
        
        total = (sumdfs(root))
        # print(f'all_sums: {all_sums} total: {total}')
        best = 0
        for s in all_sums:
            best = max(best, s * (total - s))
        return best % (10 ** 9 + 7)
        
        
# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

# Note that you need to maximize the answer before taking the mod and not after taking it.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
# Example 2:


# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

# Constraints:

# The number of nodes in the tree is in the range [2, 5 * 104].
# 1 <= Node.val <= 104