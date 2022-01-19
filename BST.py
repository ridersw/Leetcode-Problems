class BST:
    def __init__(self, data):
        self.data = data
        self.left=  None
        self.right = None

    def addChild(self, data):
        
        if data == self.data:
            return

        if data > self.data:
            #right tree
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BST(data)

        if data < self.data:
            #left tree
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BST(data)

    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTraversal()

        return elements


def helper(arr):
    root = BST(arr[0])

    for swi in range(1, len(arr)):
        root.addChild(arr[swi])

    return root

if __name__ == "__main__":
    arr = [5,1,3,6,1,9,0,4,2]

    root = helper(arr)
    print(f'root: {root.left.left.data}')

    print(root.inOrderTraversal())