class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)

    def peek(self):
        return self.data[0]







class Stack:
    def __init__(self):
        self.data = []
        self.count = 0

    def push(self, value):
        self.data.append(value)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.data.pop()

    def peek(self):
        return self.data[self.count]





if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("---------")

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

