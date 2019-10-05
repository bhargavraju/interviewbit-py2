"""
Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j
such that A[i] - A[j] = k, i != j.

"""


# @param A : list of integers
# @param B : integer
# @return an integer
def diffPossible(A, B):
    if A[-1] - A[0] < B:
        return 0
    i = 0
    j = 1
    while j < len(A):
        if A[j] - A[i] == B and i != j:
            return 1
        elif A[j] - A[i] > B:
            i += 1
        else:
            j += 1
    return 0
