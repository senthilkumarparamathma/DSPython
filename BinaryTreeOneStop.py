class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def AddItems(self, value):
        current = self
        while current != None:
            if value < current.value:
                if current.left is None:
                    current.left = BST(value)
                    break
                else:
                    current = current.left
            else:

                if current.right is None:
                    current.right = BST(value)
                    break
                else:
                    current = current.right

    # Breadth First Search . - Queue
    def bfs(self):
        current = self
        queue = []
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print("{0}".format(current.value))
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    # Depth first search  - Stack
    def dfs(self):
        current = self
        stack = []
        while stack or current:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.value)
                current = current.right

    # Depth first search  - Stack
    def dfs2(self):
        current = self
        stack = []
        # stack.append(current)
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value)
                current = current.right
            else:
                break

    # Iterative function for inorder tree traversal  = DFS (i.e use Stack)

    def containsValue(self, value):
        current = self
        queue = []
        queue.append(current)
        while queue:
            current = queue.pop(0)
            if (self.checkValue(current, value) == True):
                return True
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return False

    def findClosestNodeValue(self, value):
        current = self
        queue = []
        queue.append(current)
        minValue = abs(value - current.value)
        minValueNode = current

        while queue:
            current = queue.pop(0)
            currentMinValue = abs(value - current.value)
            if minValue > currentMinValue:
                minValue = currentMinValue
                minValueNode = current

            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
        return minValueNode.value

    def checkValue(self, node, value):
        return True if node.value == value else False

    def ValidateAndSwap2Node(self):
        current = self
        self.UtillValidateAndSwap2Node(current, float('-inf'), float('inf'), [])

    def UtillValidateAndSwap2Node(self, current, minValue, maxValue, array):
        if current == None:
            return
        value = current.value
        if value < minValue or value >= maxValue:
            if len(array) == 0:
                array.append(current)
                print("need to swap 1 : {0}".format(value))
            else:
                temp = array[0].value
                array[0].value = value
                current.value = temp
                print("need to swap 1 : {0}".format(value))

        self.UtillValidateAndSwap2Node(current.left, minValue, value, array)
        self.UtillValidateAndSwap2Node(current.right, value, maxValue, array)

    def minValueNode(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def deleteNodeByValue(self, value):
        current = self
        if current.value < value:
            current.left = self.deleteNodeByValue(current.left, value)
        elif current.value > value:
            current.right = self.deleteNodeByValue(current.right, value)
        else:
            # its means one node or no node
            # Copy the child to the node and delete the child
            if current.left is None:
                temp = current.right
                current = None
                return temp
            # its means one node or no node
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            # its means have 2 node
            # Node with two children:
            # (smallest in the right subtree)
            minNode = self.minValueNode(current.right)
            current.value = minNode.value
            current.right = self.deleteNodeByValue(current.right, minNode.value)
        return current

    # Return maximum path sum in tree with given root
    def findMaxSum(self):
        root = self
        result = [float("-inf")]
        self.findMaxUtil(root, result)
        return result[0]

    # This function returns overall maximum path sum in 'res'
    # And returns max path sum going through root
    def findMaxUtil(self, root, result):

        # Base Case
        if root is None:
            return 0

        # l and r store maximum path sum going through left
        # and right child of root respetively
        l = self.findMaxUtil(root.left, result)
        r = self.findMaxUtil(root.right, result)

        # Max path for parent call of root. This path
        # must include at most one child of root
        max_single = max(max(l, r) + root.value, root.value)

        # Max top represents the sum when the node under
        # consideration is the root of the maxSum path and
        # no ancestor of root are there in max sum path
        max_top = max(max_single, l + r + root.value)

        # Static variable to store the changes
        # Store the maximum result
        result[0] = max(result[0], max_top)

        return max_single

    def printNodeValue(self):
        current = self
        print("In Order --")
        self.inorder(current)
        print("Pre Order --")
        self.preorder(current)
        print("Post Order --")
        self.postorder(current)

    def inorder(self, current):
        if current is not None:
            self.inorder(current.left)
            print("{0}".format(current.value))
            self.inorder(current.right)

    def preorder(self, current):
        if current is not None:
            print("{0}".format(current.value))
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current is not None:
            self.postorder(current.left)
            self.postorder(current.right)
            print("{0}".format(current.value))

    '''Two of the nodes of a Binary Search Tree (BST) are swapped. Fix (or correct) the BST.'''


'''
tree = BST(1)
tree.left = BST(2)
tree.right = BST(3)
tree.left.left = BST(4)
tree.left.right = BST(5)
'''

'''

tree = BST(10)
tree.left = BST(5)
tree.right = BST(6)
tree.left.left = BST(1)
tree.left.right = BST(22)
tree.right.left = BST(12)
tree.right.right = BST(36)
'''

tree = BST(9)
tree.left = BST(4)
tree.right = BST(17)
tree.left.left = BST(3)
tree.left.right = BST(6)
tree.left.right.left = BST(5)
tree.left.right.right = BST(7)
tree.right.right = BST(22)
tree.right.right.left = BST(20)

# tree.printNodeValue()
print("bfs ---")
tree.bfs()
print("dfs ---")
tree.dfs()
print("---")
print(tree.containsValue(13))
print(tree.containsValue(6))
print('--Closset Node Value-')
print(tree.findClosestNodeValue(12))

root = BST(10)
root.left = BST(5)
root.right = BST(6)
root.left.left = BST(1)
root.left.right = BST(22)
root.right.left = BST(12)
root.right.right = BST(36)
print(root.dfs())
root.ValidateAndSwap2Node()
print(root.dfs())

# Driver program
root = BST(10)
root.left = BST(2)
root.right = BST(10);
root.left.left = BST(20);
root.left.right = BST(1);
root.right.right = BST(-25);
root.right.right.left = BST(3);
root.right.right.right = BST(4);
print("Max path sum is {0} ".format(root.findMaxSum()))
