"""
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.
Make sure the combinations are sorted.

To elaborate,
Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.

If n = 4 and k = 2, a solution is:
[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]
"""


# @param A : integer
# @param B : integer
# @return a list of list of integers
def combinations(start, n, k):
    if k == 0:
        return [[]]
    if n - start + 1 < k:
        return []
    res = []
    for i in range(start, n + 1):
        res += [[i] + x for x in combinations(i + 1, n, k - 1)]
    return res


def combine(A, B):
    return combinations(1, A, B)
