"""
Given a collection of numbers, return all possible permutations.

Example:
[1,2,3] will have the following permutations:
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
 NOTE
No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
"""


# @param A : list of integers
# @return a list of list of integers
def permute(A):
    if len(A) == 1:
        return [A]
    return_val = []
    for i in range(len(A)):
        el = A[i]
        rem = A[:i] + A[i + 1:]
        for perm in permute(rem):
            return_val.append([el] + perm)
    return return_val
