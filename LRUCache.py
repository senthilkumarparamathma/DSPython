class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddItemsFromHead(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif self.head == self.tail:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            self.tail = temp
            self.tail.previous = newNode
        else:
            temp = self.head
            self.head = newNode
            newNode.next = temp
            temp.previous = newNode

    def UpdateExistinfItemToHead(self, node):
        if self.head == node:
            return self.head
        else:
            if self.tail == node:
                self.RemoveItemFromTail()
            # remap
            prevNode = node.previous
            nextNode = node.next
            prevNode.next = nextNode
            # re Add to Head
            self.AddItemsFromHead(node)

    def RemoveItemFromTail(self):
        if self.tail == None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        temp = self.tail.previous
        self.tail = temp
        self.tail.next = None


class LRU:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.currentSize = 0
        self.linkedList = DLinkedList()
        self.hashTable = {}

    def addKeyValues(self, key, value):
        node = Node(key, value)
        # new item
        if key not in self.hashTable:
            if self.currentSize == self.maxSize:
                self.evictLeastUsed()
                self.hashTable.update({key: node})
                self.linkedList.AddItemsFromHead(node)
            else:
                self.currentSize += 1
                self.linkedList.AddItemsFromHead(node)
                self.hashTable.update({key: node})
        else:
            # Existing Item
            node = self.hashTable[key]
            node.value = value
            self.linkedList.UpdateExistinfItemToHead(node)

    def evictLeastUsed(self):
        leastUsedKey = self.linkedList.tail.key
        self.linkedList.RemoveItemFromTail()
        del self.hashTable[leastUsedKey]

    def getItems(self, key):
        node = self.hashTable[key]
        self.linkedList.UpdateExistinfItemToHead(node)
        return node.value

    def printNode(self):
        current = self.linkedList.head
        while current != None:
            print("key:{},value {} \n".format(current.key, current.value))
            current = current.next


cacheMachine = LRU(4)
cacheMachine.addKeyValues("A", "65")
cacheMachine.addKeyValues("B", "66")
cacheMachine.addKeyValues("C", "67")
cacheMachine.addKeyValues("D", "68")
cacheMachine.printNode()
print("----")
cacheMachine.addKeyValues("E", "69")
cacheMachine.printNode()

'''
print("----")
cacheMachine.addKeyValues("F","70")
cacheMachine.printNode()
'''
print('---')
result = cacheMachine.getItems("C")
cacheMachine.printNode()
print('====')
print(result)







