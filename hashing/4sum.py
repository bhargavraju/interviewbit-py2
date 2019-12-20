"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Elements in a quadruplet (a,b,c,d) must be in non-descending order.
The solution set must not contain duplicate quadruplets.

Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:

    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
    (-1,  0, 0, 1)
Also make sure that the solution set is lexicographically sorted.
"""


# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def fourSum(A, B):
    A.sort()
    sum_store = {}
    n = len(A)
    result = set()
    for i in range(n - 1):
        for j in range(i + 1, n):
            curr_sum = A[i] + A[j]
            if B - curr_sum in sum_store:
                for pair in sum_store[B - curr_sum]:
                    if pair[1] < i:  # To avoid counting the same quadruple multiple times
                        result.add((A[pair[0]], A[pair[1]], A[i], A[j]))
            if curr_sum not in sum_store:
                sum_store[curr_sum] = [(i, j)]
            else:
                sum_store[curr_sum].append((i, j))
    return sorted(map(list, result))
