# 数值的整数次方

def power(num, p):
    if p == 0:
        return 1

    if p == 1:
        return num
    
    inverse = -1 if p < 0 else 1
    p *= inverse

    half = power(num, p >> 1)
    result = half * half
    if p & 1 == 1:
        result *= num

    if inverse == -1:
        result = 1 / result

    return result

if __name__ == '__main__':
    print(power(-2, -3))
