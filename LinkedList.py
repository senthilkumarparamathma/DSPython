class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        node = Node(data)
        self.head = node

    def addItem(self, data):
        node = Node(data)
        current = self.head
        # current.next = node
        while current.next != None:
            current = current.next
        current.next = node

    def findNode(self, data):
        current = self.head
        while current.data != data:
            current = current.next
        if current.data == data:
            return current
        return None

    def insertItemAfter(self, data, dataAfter):
        node = Node(data)
        resultNode = self.findNode(dataAfter)
        temp = resultNode.next
        node.next = temp
        resultNode.next = node

    def removeItem(self, data):
        deleteNode = self.findNode(data)
        newNextNode = deleteNode.next
        previousNode = self.findPrevious(data)
        previousNode.next = newNextNode

    def findPrevious(self, data):
        current = self.head
        while current.next != None and current.next.data != data:
            current = current.next
        return current

    def printNode(self):
        current = self.head
        while current != None:
            print("{},".format(current.data))
            current = current.next

    def removeKthNodeFromEnd(self, k):
        # Write your code here.
        root = self.head.next
        behindNode = root  #
        forwardNode = root

        index = 1
        while index <= k:
            forwardNode = forwardNode.next
            index += 1

        if forwardNode is None:
            root = behindNode.next
            return
        # behindnode k mode behnind from forward Node
        while forwardNode.next != None:
            behindNode = behindNode.next
            forwardNode = forwardNode.next
        behindNode.Next = behindNode.next.next


LL = LinkedList("*")
LL.addItem(1)
LL.addItem(2)
LL.addItem(3)
LL.addItem(4)
LL.addItem(5)
LL.addItem(6)
LL.addItem(7)
LL.addItem(8)
LL.addItem(9)
LL.printNode()
LL.removeKthNodeFromEnd(4)
LL.printNode()
'''
LL.insertItemAfter(12, 10)
print("---")
LL.printNode()
print("------------")
LL.removeItem(14)
LL.printNode()
'''








