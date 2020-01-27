class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class NodeList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(value)

    def delete(self, i):
        cur = self.head
        count = 0
        while cur != None and count < i - 1:
            cur = cur.next
            count += 1
        
        obj = cur.next
        cur.next = obj.next
        del(obj)

    def findAndDelete(self, value):
        if self.head == None:
            return

        cur = self.head
        pre = None
        while cur != None:
            if cur.value == value:
                if cur == self.head:
                    self.head = self.head.next
                else:
                    pre.next = cur.next
            
                del(cur)
                break
            pre = cur
            cur = cur.next

    def display(self):
        cur = self.head
        while cur != None:
            print(cur.value, end=' ')
            cur = cur.next
        print()

    def reverse(self):
        self.reverse_display(self.head)

    def reverse_display(self, node):
        if node != None:
            self.reverse_display(node.next)
            print(node.value, end=' ')
            if node == self.head:
                print()
        else:
            return


if __name__ == '__main__':
    head = Node(1)
    demo = NodeList(head)
    for i in range(2, 10):
        demo.append(i)
    demo.display()

    demo.delete(4)
    demo.display()
    demo.findAndDelete(7)
    demo.display()
    demo.findAndDelete(1)
    demo.display()
    demo.reverse()

    head2 = Node(None)
    demo2 = NodeList(head2)
    demo.reverse()