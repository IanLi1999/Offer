# 两个队列形成一个栈

class Stack:
    def __init__(self):
        self.queue = []
        self.temp = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if len(self.queue) < 1:
            return None

        while len(self.queue) > 1:
            self.temp.append(self.queue.pop(0))
        
        cur = self.queue.pop(0)

        while len(self.temp) > 0:
            self.queue.append(self.temp.pop(0))

        return cur

if __name__ == '__main__':
    stack = Stack()
    for i in range(0, 5):
        stack.push(i)

    for i in range(0, 7):
        print(stack.pop())
