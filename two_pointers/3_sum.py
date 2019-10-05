"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution
"""


# @param A : list of integers
# @param B : integer
# @return an integer
def threeSumClosest(A, B):
    A.sort()
    n=len(A)
    res = float('inf')
    for i in xrange(0,n-2):
        left = i+1
        right = n-1
        while left<right:
            s = A[i] + A[left] + A[right]
            if abs(res-B) > abs(s-B):
                res = s
            if s == B:
                return B
            if s > B:
                right-=1
            else:
                left+=1
    return res
