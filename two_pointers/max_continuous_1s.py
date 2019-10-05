"""
You are given with an array of 1s and 0s. And you are given with an integer M, which signifies number of flips allowed.
Find the position of zeros which when flipped will produce maximum continuous series of 1s.

For this problem, return the indices of maximum continuous series of 1s in order.
"""


# @param A : list of integers
# @param B : integer
# @return a list of integers
def maxone(A, B):
    i = j = besti = bestj = 0
    while j < len(A):
        if A[j] == 0:
            B -= 1
            while i <= j and B < 0:
                B += 1 if A[i] == 0 else 0
                i += 1
        j += 1
        if j - i > bestj - besti:
            besti, bestj = i, j
    return range(besti, bestj)

# Different from kadane's algorithm (continuous sub array with max sum)
