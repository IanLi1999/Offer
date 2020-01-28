# 调整数组顺序使奇数位于偶数前面
class Solution:
    def __init__(self):
        pass

    def adjust(self, nums):
        i = 0
        j = len(nums) - 1

        while i < j:
            while i < j and (nums[i] & 1 == 1):
                i += 1
            while i < j and (nums[j] & 1 == 0):
                j -= 1
            
            # swap i and j
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        return nums

if __name__ == '__main__':
    solution = Solution()
    nums = solution.adjust([])
    print(nums)