"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained
( Yes, we know maximum area instead of maximum volume sounds weird.
But this is 2D plane we are working with for simplicity ).

"""


# @param A : list of integers
# @return an integer
def maxArea(A):
    if not A:
        return 0
    max_area = 0
    left = 0
    right = len(A) - 1
    while left < right:
        height = min(A[left], A[right])
        area = height * (right - left)
        if area > max_area:
            max_area = area
        while left < right and A[left] <= height:
            left += 1
        while left < right and A[right] <= height:
            right -= 1
    return max_area

# Note 1: When you consider a1 and aN, then the area is (N-1) * min(a1, aN).
# Note 2: The base (N-1) is the maximum possible.
# This implies that if there was a better solution possible, it will definitely have height greater than min(a1, aN).
#
# B * H > (N-1) * min(a1, aN)
# We know that, B < (N-1)
# So, H > min(a1, aN)
#
# This means that we can discard min(a1, aN) from our set and look to solve this problem again from the start.
# If a1 < aN, then the problem reduces to solving the same thing for a2, aN.
# Else, it reduces to solving the same thing for a1, aN-1
