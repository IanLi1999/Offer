# 反转链表

class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class NodeList:
    def __init__(self, head):
        self.head = head

    def reverse(self):
        if self.head == None:
            return None
        
        pre = None
        cur = self.head
        after = cur.next

        while after != None:
            cur.next = pre
            pre = cur
            cur = after
            after = after.next      
        cur.next = pre
        
        return cur


    def print_list(self):
        cur = self.head
        while cur != None:
            print(cur.elem, end='')
            cur = cur.next
        print()
        
if __name__ == '__main__':
    head = Node(1)
    test = NodeList(head)
    cur = head
    for i in range(2, 10):
        node = Node(i)
        cur.next = node
        cur = cur.next
    test.print_list()

    test.head = test.reverse()
    test.print_list()