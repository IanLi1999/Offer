# 二维数组查找
class Solution:
    def __init__(self):
        pass

    def find(self, mat, num):
        i = 0

        if type(mat) == list:
            if len(mat) >= 1:
                j = len(mat[0]) - 1
            else:
                return False

            while i < len(mat) and j >= 0:
                if mat[i][j] > num:
                    j -= 1

                elif mat[i][j] == num:
                    return True
                
                else:
                    i += 1
        
        return False


if __name__ == '__main__':
    solution = Solution()
    test = [[1, 2, 8, 9],
            [3, 4, 6, 12],
            [4, 7, 10, 13],
            [6, 8, 11, 15]]
    result = solution.find(test, 3)
    print(result)
