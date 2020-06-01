"""
Given an unsorted integer array, find the first missing positive integer.

Example:

Given [1,2,0] return 3,

[3,4,-1,1] return 2,

[-8, -7, -6] returns 1

Your algorithm should run in O(n) time and use constant space.
"""


# @param A : list of integers
# @return an integer
def firstMissingPositiveNew(A):
    n = len(A)
    one_exists = False
    for i in range(n):
        if A[i] == 1:
            one_exists = True
        elif A[i] <= 0 or A[i] > n:
            A[i] = 1

    if not one_exists:
        return 1

    for i in range(n):
        idx = abs(A[i]) - 1
        if A[idx] > 0:
            A[idx] = -1 * A[idx]

    for i in range(n):
        if A[i] > 0:
            return i + 1

    return n + 1


def firstMissingPositive(A):
    n = len(A)
    i, j = 0, n
    while i < j:
        if A[i] > 0:
            j -= 1
            A[i], A[j] = A[j], A[i]
        else:
            i += 1
    if j == n:
        return 1
    i = j
    while i < n:
        posNum = A[i] if A[i] > 0 else -A[i]
        if j + posNum - 1 < n and A[j + posNum - 1] > 0:
            A[j + posNum - 1] *= -1
        i += 1
    i = j
    while i < n:
        if A[i] > 0:
            break
        i += 1
    return i - j + 1

