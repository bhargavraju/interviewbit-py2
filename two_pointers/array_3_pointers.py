"""
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

"""


# @param A : tuple of integers
# @param B : tuple of integers
# @param C : tuple of integers
# @return an integer
def minimize(A, B, C):
    i = j = k = 0
    min_diff = float("inf")
    while i < len(A) and j < len(B) and k < len(C):
        diff = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
        min_diff = min(diff, min_diff)
        min_elem = min(A[i], B[j], C[k])
        if min_elem == A[i]:
            i += 1
        elif min_elem == B[j]:
            j += 1
        else:
            k += 1
    return min_diff
