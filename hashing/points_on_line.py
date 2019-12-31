"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :
(1, 1)
(2, 2)
Sample Output :
2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])

Note: There may be duplicate points
"""
from collections import defaultdict
from sys import maxsize


# @param A : list of integers
# @param B : list of integers
# @return an integer
def maxPoints(A, B):
    if len(A) <= 2:
        return len(A)

    max_length = 0
    n = len(A)
    for i in range(n - 1):
        x, y = A[i], B[i]
        slope_store = defaultdict(int)
        same_point = 0
        for j in range(i + 1, n):
            a, b = A[j], B[j]
            if (a, b) == (x, y):
                same_point += 1
                continue
            num = float(b - y)
            den = float(a - x)
            slope = num / den if den != 0 else maxsize
            slope_store[slope] += 1
        max_points = (max(slope_store.values()) if len(slope_store) > 0 else 0) + 1 + same_point
        max_length = max(max_points, max_length)
    return max_length
