class binaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		
	def addChild(self, data):
		if self.data == data:
			return 
			
		if self.data < data:
			#right tree
			if self.right:
				self.right.addChild(data)
			else:
				self.right = binaryTree(data)
				
		else:
			#left tree
			if self.left:
				self.left.addChild(data)
			else:
				self.left = binaryTree(data)
	
	def preOrderTraversal(self):
		elements = []
		
		elements.append(self.data)
		
		if self.left:
			elements += self.left.preOrderTraversal()
			
		if self.right:
			elements += self.right.preOrderTraversal()
			
		return elements	
		
		
	def inOrderTraversal(self):
		elements = []
		
		if self.left:
			elements += self.left.inOrderTraversal()
			
		elements.append(self.data)

		if self.right:
			elements += self.right.inOrderTraversal()
			
		return elements	
		
		
	def postOrderTraversal(self):
		elements = []
		
		if self.left:
			elements += self.left.postOrderTraversal()
			
		if self.right:
			elements += self.right.postOrderTraversal()
			
		elements.append(self.data)

		return elements	

def treeBuilder(numberArray):
	
	root = binaryTree(numberArray[0])
	
	for swi in range(1, len(numberArray)):
		root.addChild(numberArray[swi])
		
	return root	

if __name__ == "__main__":
	numberArray = [15,12,27,7,14,20,88,23]	
	
	root = treeBuilder(numberArray)
	
	print(f'root: {root.right.data}')
	
	print(f'preOrderTraversal: {root.preOrderTraversal()}')
	print(f'inOrderTraversal: {root.inOrderTraversal()}')
	print(f'postOrderTraversal: {root.postOrderTraversal()}')
	
#Construct the binary Tree and write program for traversals	