def prettyPrint(A):
    if A == 1:
        return [[1]]
    n, l, num = 2 * A - 1, 0, A
    arr = [[0] * n for i in range(n)]
    while l < A:
        for i in range(l, n-l):
            arr[l][i] = arr[i][n-l-1] = arr[n-l-1][n-1-i] = arr[n-1-i][l] = num
        num -= 1
        l += 1
    return arr


ans = prettyPrint(1)
print ans
