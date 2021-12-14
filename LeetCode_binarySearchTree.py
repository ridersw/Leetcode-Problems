class Solution:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if self.data == data:
            return

        if self.data > data:
            if self.left:
                return self.left.addChild(data)
            else:
                self.left = Solution(data)
        else:
            if self.right:
                return self.right.addChild(data)
            else:
                self.right = Solution(data)

    def preOrderTraversal(self):

        elements = []
        
        if self.left:
            elements += self.left.preOrderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.preOrderTraversal()

        return elements


def helperFunction(arr):
    root = Solution(arr[0])

    for swi in range(1, len(arr)):
        root.addChild(arr[swi])

    return root

if __name__ == "__main__":
    arr = [10,5,15,3,7,18]

    root = helperFunction(arr)

    print(root.preOrderTraversal())