"""
You are given an array (zero indexed) of N non-negative integers, A0, A1, A2, .....An-1.Find the minimum sub array
Al, Al+1, ......Ar o if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:
A = [1, 3, 2, 4, 5]
Return: [1, 2]

Input 2:
A = [1, 2, 3, 4, 5]
Return: [-1]

In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
"""


# @param A : list of integers
# @return a list of integers
def subUnsort(A):
    n = len(A)
    if n <= 1:
        return [-1]
    l, r = 0, n - 1
    while l < n - 1 and A[l] <= A[l + 1]:
        l += 1
    while r > 0 and A[r] >= A[r - 1]:
        r -= 1
    if l > r:
        return [-1]
    sub_arr = A[l: r + 1]
    min_val, max_val = min(sub_arr), max(sub_arr)
    for i in range(l - 1, -1, -1):
        if A[i] > min_val:
            l -= 1
        else:
            break
    for i in range(r + 1, n):
        if A[i] < max_val:
            r += 1
        else:
            break
    return [l, r]
