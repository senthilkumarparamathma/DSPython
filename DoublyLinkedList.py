class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DLinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node

    def addItem(self, data):
        newNode = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        newNode.previous = current

    def findItem(self, data):
        current = self.head
        while current.data != data:
            current = current.next
        return current

    def removeItem(self, data):
        delNode = self.findItem(data)
        prevNode = delNode.previous
        nextNode = delNode.next

        prevNode.next = nextNode
        nextNode.previous = prevNode

    def insertItemAfter(self, data, dataAfter):
        newNode = Node(data)
        afterNode = self.findItem(dataAfter)

        movingNode = afterNode.next
        afterNode.next = newNode
        newNode.previous = afterNode
        newNode.next = movingNode
        movingNode.previous = newNode

    def printNode(self):
        current = self.head
        while current != None:
            print("{},".format(current.data))
            current = current.next


LL = DLinkedList("*")
LL.addItem(10)
LL.addItem(13)
LL.addItem(14)
LL.addItem(15)
LL.printNode()
print("---")

LL.insertItemAfter(12, 10)
print("---")
LL.printNode()

print("------------")
LL.removeItem(14)
LL.printNode()










