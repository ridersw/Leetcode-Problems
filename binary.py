class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if self.data == data:
            return
        
        if self.data < data:
            #right
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BST(data)

        if self.data > data:
            #right
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BST(data)

    def displayTree(self):
        elements =[]

        if self.left:
            elements += self.left.displayTree()

        elements.append(self.data)

        if self.right:
            elements += self.right.displayTree()

        return elements



def helper(array):
    root = BST(array[0])

    for swi in range(1,len(array)):
        root.addChild(array[swi])

    return root

if __name__ == "__main__":
    array = [4,3,2,1,9,8,7,6,5]

    root = helper(array)

    print(f'root: {root.data}')

    print(root.displayTree())