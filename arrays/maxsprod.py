"""
You are given an array A containing N integers. The special product of each ith integer in this array is defined as
the product of the following:

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j] s are
present in multiple positions, the LeftSpecialValue is the maximum value of j.

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are
present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.
Input: You will receive array of integers as argument to function.
Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
"""


def nearestGT(A):
    res = []
    stack = []
    for i, x in enumerate(A):
        while stack and stack[-1][1] <= x:
            stack.pop()
        k = stack[-1][0] if stack else -1
        res.append(k)
        stack.append((i, x))
    return res


# @param A : list of integers
# @return an integer
def maxSpecialProduct(A):
    if not A:
        return 0
    MODU = 1000000007
    n = len(A)
    rightmost = [n - 1 - j if j >= 0 else 0 for j in nearestGT(reversed(A))]
    rightmost.reverse()
    leftmost = (max(0, j) for j in nearestGT(A))
    return max(j * k for j, k in zip(leftmost, rightmost)) % MODU
