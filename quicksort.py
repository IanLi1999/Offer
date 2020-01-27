def partition(nums, start, end):
    i = start
    j = end

    pivot = nums[i]

    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]

        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]

    nums[i] = pivot
    return i

def quicksort(nums, start, end):
    if start == end:
        return

    index = partition(nums, start, end)
    if index > start:
        quicksort(nums, start, index - 1)
    if index < end:
        quicksort(nums, index + 1, end)


if __name__ == '__main__':
    demo = [2,5,1,2,7,4,56,28,13,56,24,3]
    quicksort(demo, 0, len(demo)-1)
    print(demo)