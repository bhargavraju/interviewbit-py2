"""
Given an index k, return the kth row of the Pascal's triangle.

Pascal's Triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?
"""


# @param A : integer
# @return a list of integers
def getRow(A):
    x = [1] * (A + 1)
    for i in range(1, A):
        x[i] = int(x[i - 1] * (A + 1 - i) / i)
    return x
