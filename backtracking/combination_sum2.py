"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ..., ak) must be in non-descending order.
The solution set must not contain duplicate combinations.

Given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""


# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def combinationSum(A, B):
    A.sort()
    res = []
    rec(A, [], B, res)
    return res


def rec(arr, curr, lim, res):
    if sum(curr) > lim:
        return
    if sum(curr) == lim:
        res.append(curr)
        return
    i = 0
    while i < len(arr):
        rec(arr[i + 1:], curr + [arr[i]], lim, res)
        j = i  # Skipping all possible duplicate combinations
        while j < len(arr) and arr[i] == arr[j]:
            j += 1
        i = j
