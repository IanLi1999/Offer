# 重建二叉树
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        pass

    def build(self, pre, inorder):
        if len(pre) == 0 or len(pre) != len(inorder):
            return
        root = Node(pre[0])
        mid = inorder.index(pre[0])
        root.left = self.build(pre[1: mid+1], inorder[0: mid])
        root.right = self.build(pre[mid+1:], inorder[mid+1:])
        return root


if __name__ == '__main__':
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    solution = Solution()
    tree = solution.build(preorder, inorder)
    print('done')
