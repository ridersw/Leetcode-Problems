# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = -1
        self.bottomLeftValue = 0
        self.dfs(root, 0)
        return self.bottomLeftValue
    
    def dfs(self, current, depth):
        if not current:
            return 
        
        if depth > self.maxDepth:
            self.maxDepth = depth
            self.bottomLeftValue = current.val
            
        self.dfs(current.left, depth + 1)
        self.dfs(current.right, depth + 1)
        return
    
# Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

# Example 1:


# Input: root = [2,1,3]
# Output: 1
# Example 2:


# Input: root = [1,2,3,4,null,5,6,null,null,7]
# Output: 7
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1