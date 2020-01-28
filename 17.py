# 合并两个排序的链表
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class NodeList:
    def __init__(self, head):
        self.head = head

    def merge(self, listB):
        pA = self.head
        pB = listB.head
        mList = NodeList(None)
        p = None

        while pA != None and pB != None:
            if pA.elem <= pB.elem:
                num = pA.elem
                pA = pA.next
            else:
                num = pB.elem
                pB = pB.next

            if p == None:
                mList.head = Node(num)
                p = mList.head
            else:
                p.next = Node(num)
                p = p.next

        cur = None

        if pA != None:
            cur = pA
        if pB != None:
            cur = pB

        while cur != None:
            if p == None:
                mList.head = Node(cur.elem)
                p = mList.head
            else:
                p.next = Node(cur.elem)
                p = p.next
            
            cur = cur.next

        return mList


    def print_list(self):
        cur = self.head
        while cur != None:
            print(cur.elem, end='')
            cur = cur.next
        print()


if __name__ == '__main__':
    # A = [1,3,4,5,6,9]
    # B = [2,5,6,7,8]
    A = B = []
    
    curA = Node(0)
    listA = NodeList(curA)
    for i in A:
        curA.next = Node(i)
        curA = curA.next
        
    curB = Node(1)
    listB = NodeList(curB)
    for i in B:
        curB.next = Node(i)
        curB = curB.next

    listA.print_list()
    listB.print_list()

    listC = listA.merge(listB)
    listC.print_list()

    ListD = NodeList(None)
    ListE = NodeList(None)
    ListF = ListD.merge(ListE)
    ListF.print_list()

    temp = NodeList(Node(0))
    ListG = temp.merge(ListD)
    ListG.print_list()
