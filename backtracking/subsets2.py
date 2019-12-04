"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.

If S = [1,2,2], the solution is:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]

Hint: Try solving this on paper with a simple case containing duplicates
"""


# @param A : list of integers
# @return a list of list of integers
def subsetsWithDup(A):
    A.sort()
    res = [[]]
    i = 0
    while i < len(A):
        new = [x + [A[i]] for x in res]
        res += new
        j = i + 1
        while j < len(A) and A[i] == A[j]:
            new = [x + [A[i]] for x in new]
            res += new
            j += 1
        i = j
    return sorted(res)
