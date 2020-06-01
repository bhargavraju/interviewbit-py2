"""
Given an array A of integers, find the maximum of j - i subjected to the constraint of A[i] <= A[j].
If there is no solution possible, return -1.

Example :
A : [3 5 4 2]

Output : 2
for the pair (3, 4)
"""


# @param A : tuple of integers
# @return an integer
def maximumGap(A):
    n = len(A)
    if n <= 1:
        return 0
    l_min, r_max = [0] * n, [0] * n
    l_min[0] = A[0]
    for i in range(1, n):
        l_min[i] = min(A[i], l_min[i - 1])
    r_max[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        r_max[i] = max(A[i], r_max[i + 1])
    i, j = 0, 0
    diff = -1
    while i < n and j < n:
        if l_min[i] <= r_max[j]:
            diff = max(diff, j - i)
            j += 1
        else:
            i += 1
    return diff
