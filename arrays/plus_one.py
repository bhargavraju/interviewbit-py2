arr = [9, 9, 9, 9, 9]


def plus_one(A):
    n = len(A)
    carry = 1
    for i in xrange(n - 1, -1, -1):
        sum = A[i] + carry
        A[i] = sum % 10
        carry = sum // 10
    if carry > 0:
        return A.insert(0, carry)
    while len(A) > 0 and A[0] == 0:
        del A[0]
    return A


ans = plus_one(arr)
print ans