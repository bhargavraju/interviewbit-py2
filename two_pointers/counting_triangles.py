"""
You are given an array of N non-negative integers, A0, A1, .... An-1
Considering each array element Ai as the edge length of some line segment,
count the number of triangles which you can form using these array values.

"""


# @param A : list of integers
# @return an integer
def nTriang(A):
    A.sort()
    res = 0
    n = len(A)
    for i in range(n-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            s = A[j] + A[k]
            if s > A[i]:
                res += k-j
                k -= 1
            else:
                j += 1
    return res%(10**9 + 7)
