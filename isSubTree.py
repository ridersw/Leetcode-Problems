# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None:
            return False
        
        if self.helper(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def helper(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        
        if root == None or subRoot == None or root.val != subRoot.val:
            return False
        
        return (self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right))
        
        