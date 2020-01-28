class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class NodeList:
    def __init__(self, head):
        self.head = head

    def deleteNode(self, node):
        temp = node.next

        if temp == None:
            if self.head == node:
                self.head = None
                del(node)
                return

            cur = self.head
            while cur.next != node:
                cur = cur.next
            del(node)
            cur.next = None
        else:
            node.elem = temp.elem
            node.next = temp.next
            del(temp)

    def print_list(self):
        cur = self.head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()


if __name__ == '__main__':
    head = Node(1)
    cur = head
    demo = NodeList(head)
    nodes = [head]
    for i in range(2, 10):
        node = Node(i)
        nodes.append(node)
        cur.next = node
        cur = cur.next
    
    demo.print_list()

    demo.deleteNode(nodes[3])
    demo.print_list()

    demo.deleteNode(nodes[-1])
    demo.print_list()

    demo.deleteNode(nodes[0])
    demo.print_list()

    head2 = Node(1)
    demo = NodeList(head2)
    demo.deleteNode(head2)
    demo.print_list()

