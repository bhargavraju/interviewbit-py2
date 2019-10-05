"""
Given three sorted arrays A, B and Cof not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c
such that a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

"""


def solve(A, B, C):
    i, j, k = len(A) - 1, len(B) - 1, len(C) - 1
    min_diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
    while i >= 0 and j >= 0 and k >= 0:
        diff = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
        min_diff = min(min_diff, diff)
        max_term = max(A[i], B[j], C[k])
        if max_term == A[i]:
            i -= 1
        elif max_term == B[j]:
            j -= 1
        else:
            k -= 1
    return min_diff
