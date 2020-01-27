# 旋转数组的最小元素 

class Solution:
    def __init__(self):
        pass

    def find_min(self, nums):
        i = 0
        j = len(nums) - 1

        pivot = nums[0]
        
        while j - i > 1:
            mid = int(i + (j - i) / 2)
            if nums[mid] >= pivot:
                i = mid
            else:
                j = mid

        return nums[j]

if __name__ == '__main__':
    # demo = [5,6,7,8,1,2,3,4]
    # demo = [7,8,2,3,4,5,6,7]
    demo = [2,3,4,5,5,6,7,1]
    solution = Solution()
    print(solution.find_min(demo))
