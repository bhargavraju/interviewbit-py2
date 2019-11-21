"""
Given an array of integers A of size N. A represents a histogram i.e.. A[i] denotes the height of ith histogram bar
Width of each bar is 1.
Find the area of largest rectangle in the histogram.

Refer: Internet sources for better understanding of problem and solution
"""


# @param A : list of integers
# @return an integer
def largestRectangleArea(A):
    stack = []
    n = len(A)
    max_area = 0
    i = 0
    while i < n:
        if len(stack) == 0 or A[i] >= A[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            tp = stack.pop()
            area_with_top = A[tp] * (i if len(stack) == 0 else i - stack[-1] - 1)
            max_area = max(max_area, area_with_top)
    while len(stack) != 0:
        tp = stack.pop()
        area_with_top = A[tp] * (n if len(stack) == 0 else n - stack[-1] - 1)
        max_area = max(max_area, area_with_top)
    return max_area
