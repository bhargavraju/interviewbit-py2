def rotate(A):
    n = len(A)
    l = 0
    while l < n / 2:
        for i in range(l, n-1-l):
            A[l][i], A[i][n-1-l], A[n-1-l][n-1-i], A[n-1-i][l] = A[n-1-i][l], A[l][i], A[i][n-1-l], A[n-1-l][n-1-i]
        l += 1
    return A


arr = [
  [31, 32, 228, 333],
  [79, 197, 241, 246],
  [77, 84, 126, 337],
  [110, 291, 356, 371]
]

ans = rotate(arr)
print ans
