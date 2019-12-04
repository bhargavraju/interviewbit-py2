"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, .....ak) must be in non-descending order.
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) or (a1 == b1 and a2 > b2) or (a1 == b1, a2 == b2 and a3 > b3) ......
The solution set must not contain duplicate combinations.

Given candidate set 2,3,6,7 and target 7,
A solution set is:
[2, 2, 3]
[7]
"""


# @param A : list of integers
# @param B : integer
# @return a list of list of integers
def combinationSum(A, B):
    A = list(set(A))
    A.sort()
    res = []
    rec(A, [], B, res)
    return res


def rec(ar, cur, lim, res):
    if sum(cur) > lim:
        return
    if sum(cur) == lim:
        res.append(cur)
        return
    for i in range(len(ar)):
        rec(ar[i:], cur + ar[i:i + 1], lim, res)
