# 合并两个有序数组 
class Solution:
    def __init__(self):
        pass

    def merge(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        k = i + j + 1
        a = a + b
        while i >= 0 and j >= 0:
            if a[i] >= b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1

        while k >= 0 and i < 0:
            a[k] = b[j]
            j -= 1
            k -= 1
        
        return a

if __name__ == '__main__':
    solution = Solution()
    n1 = [3,5,8,10,12]
    n2 = [1, 2, 4,17,32]
    result = solution.merge(n1, n2)
    print(result)