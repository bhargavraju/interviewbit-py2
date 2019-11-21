"""
Given an array of integers A. There is a sliding window of size B which
is moving from the very left of the array to the very right.
You can only see the w numbers in the window. Each time the sliding window moves
rightwards by one position. You have to find the maximum for each window.

Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].
Note: If B > length of the array, return 1 element with the max of the array.

Note: Don't go by the obvious constant window max valuing approach. It is not O(n).
Refer interviewbit solution approach and internet to get the gist of the problem approach
"""


# @param A : tuple of integers
# @param B : integer
# @return a list of integers
def slidingMaximum(A, B):
    n = len(A)
    if B >= n:
        return [max(A)]
    deq = []
    res = []
    for i in range(n):
        if i >= B:
            if deq[0] == A[i - B]:
                deq.pop(0)
        while deq and A[i] > deq[-1]:
            deq.pop()
        deq.append(A[i])
        if i >= B - 1:
            res.append(deq[0])
    return res
