# 二进制中1的个数

def count_one(num):
    count = 0 if num >= 0 else 1
    num = abs(num)
    while(num):
        count += 1
        n = num - 1
        num = n & num
    return count

def is_power(num):
    return (num & (num - 1) == 0)

def change(m, n):
    diff = m ^ n
    return count_one(diff)

if __name__ == '__main__':
    print(count_one(0))
    print(is_power(9))
    print(change(12, 0))