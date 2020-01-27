# 用两个栈实现队列

class Queue:
    def __init__(self):
        self.stack = []
        self.temp = []

    def appendTail(self, value):
        self.stack.append(value)

    def deleteHead(self):
        if len(self.stack) < 1:
            return None

        while len(self.stack) > 1:
            self.temp.append(self.stack.pop())
        
        cur = self.stack.pop()

        while len(self.temp) > 0:
            self.stack.append(self.temp.pop())
        
        return cur

if __name__ == '__main__':
    queue = Queue()
    for i in range(0, 5):
        queue.appendTail(i)

    for i in range(0, 7):
        print(queue.deleteHead())

