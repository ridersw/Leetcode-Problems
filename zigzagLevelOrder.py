# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        level, todo, ans = 0, [(root, 0)], collections.defaultdict(list)
        
        while todo:
            node, level = todo.pop()
            
            if level % 2:
                ans[level].append(node.val)
            else:
                ans[level].insert(0, node.val)
                
            if node.left:
                todo.append((node.left, level + 1))
            if node.right:
                todo.append((node.right, level + 1))
                
        return ans.values()

# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100