from email import header


class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head= None

    
    def printList(self):
        temp = self.head

        while temp:
            print(temp.data + ' --> ', end='')
            temp = temp.next
        print('None')

if __name__ == "__main__":
    obj = linklist()

    obj.head = node('first')
    obj.head.next = node('second')

    obj.printList()