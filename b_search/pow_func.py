def pow(x, n, d):
    res = 1 % d
    while n > 0:
        if n & 1:
            res = (res * x) % d
        x = x ** 2 % d
        n >>= 1
    return res


ans = pow(3, 8, 10000000)
print ans
