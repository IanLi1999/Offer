class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class NodeList:
    def __init__(self, head):
        self.head = head

    def findLastK(self, k):
        if self.head == None:
            return None

        p_node = self.head
        k_node = self.head
        for i in range(1, k):
            p_node = p_node.next
            if p_node == None:
                return None

        while p_node.next != None:
            p_node = p_node.next
            k_node = k_node.next
        
        return k_node

    def find_middle(self):
        if self.head == None:
            return None

        p_node = self.head
        m_node = self.head

        while p_node.next != None:
            p_node = p_node.next
            if p_node.next == None:
                break
            p_node = p_node.next

            m_node = m_node.next

        return m_node

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

    print(test.findLastK(4).elem)
    print(test.findLastK(10))
    
    test2 = NodeList(None)
    print(test2.findLastK(2))

    test3 = NodeList(Node(1))
    print(test3.findLastK(2))

    print(test.find_middle().elem)
    print(test2.find_middle().elem)
