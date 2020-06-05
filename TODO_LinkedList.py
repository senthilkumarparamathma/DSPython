'''
1)  Circular linkled list
2)  Intersections of linkedlist - 2 linked list

'''

class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self,data):
        node = Node(data)
        self.head = node

    def addItems(self,data):
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data)

    def setCyleForTest(self,data):
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data)
        current.next.next = self.head

    def printItems(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



    def isCircle(self):
        regular = self.head
        speed = self.head
        while regular and speed and speed.next:
            regular = regular.next
            speed = speed.next.next

            if regular == speed:
              return  True

        return  False







ll = LinkedList(10)
ll.addItems(11)
ll.addItems(12)
ll.addItems(13)
ll.addItems(14)
ll.setCyleForTest(15)
# ll.printItems()
print(ll.isCircle())