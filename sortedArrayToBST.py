class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None
			
		mid = len(nums) // 2
		print(f'mid: {nums[mid]}')
		root = TreeNode(nums[mid])
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid+1:])
		
		return root
		
	
if __name__ == "__main__":
	nums = [-10,-3,0,5,9]
	
	obj = Solution()
	
	root = obj.sortedArrayToBST(nums)

	print(f'root: {root}')	
	
	
#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

#Example 1:

#Input: nums = [-10,-3,0,5,9]
#Output: [0,-3,9,-10,null,5]
#Explanation: [0,-10,5,null,-3,null,9] is also accepted:

#Example 2:

#Input: nums = [1,3]
#Output: [3,1]
#Explanation: [1,3] and [3,1] are both a height-balanced BSTs.	