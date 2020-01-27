# 斐波那契数列
def calc(n):
    record = [0 for i in range(0, n)]
    for i in range(0, n):
        if i == 0:
            continue
        
        if i == 1:
            record[i] = 1
            continue
        
        record[i] = record[i-1] + record[i-2]
    return record[n-2] + record[n-1]

if __name__ == '__main__':
    print(calc(100))
