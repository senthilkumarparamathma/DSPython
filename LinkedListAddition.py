class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.node = Node(data)

    def addItems(self, data):
        current = self.node
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def printData(self):
        current = self.node
        while current != None:
            print("{0},".format(current.data))
            current = current.next


def addition(l1, l2):
    carryOver = 0
    l3 = None
    l1Current = l1.node
    l2Current = l2.node
    while l1Current != None or l2Current != None:
        data1 = l1Current.data if l1Current != None else 0
        data2 = l2Current.data if l2Current != None else 0
        total = data1 + data2 + carryOver
        carryOver = 1 if total >= 10 else 0
        total = total if total < 10 else total % 10

        l1Current = l1Current.next if l1Current != None else None
        l2Current = l2Current.next if l2Current != None else None

        if l3 == None:
            l3 = LinkedList(total)
        else:
            l3.addItems(total)

    l3.printData()


if __name__ == "__main__":
    l1 = LinkedList(2)
    l1.addItems(4)
    l1.addItems(3)
    l1.printData()

    l2 = LinkedList(5)
    l2.addItems(6)
    l2.addItems(4)
    #l2.addItems(1)
    print('----')
    addition(l1, l2)




