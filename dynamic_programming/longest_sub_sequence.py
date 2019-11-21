"""
Given an array of integers, A of length N, find the length of longest sub-sequence
which is first increasing then decreasing.

Input 1:
    A = [1, 2, 1]

Output 1:
    3

Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]

Output 2:
    6

Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
"""


def longestSubsequenceLength(A):
    n = len(A)
    increasing = [1] * n
    decreasing = [1] * n
    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j] and increasing[i] < increasing[j] + 1:
                increasing[i] = increasing[j] + 1
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if A[i] > A[j] and decreasing[i] < decreasing[j] + 1:
                decreasing[i] = decreasing[j] + 1
    max_length = 0
    for idx in range(n):
        max_length = max(max_length, increasing[idx] + decreasing[idx] - 1)
    return max_length


test_data = [1, 2, 3, 4, 5]
print longestSubsequenceLength(test_data)
