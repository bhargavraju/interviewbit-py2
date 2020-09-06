"""
Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers for
a given array A of size N. If such arrangement is not possible, it must be rearranged as the lowest possible order
i.e., sorted in an ascending order.

Input Format:
The first and the only argument of input has an array of integers, A.

Output Format:
Return an array of integers, representing the next permutation of the given array.

Constraints:
1 <= N <= 5e5
1 <= A[i] <= 1e9

Examples:

Input 1:
    A = [1, 2, 3]

Output 1:
    [1, 3, 2]

Input 2:
    A = [3, 2, 1]

Output 2:
    [1, 2, 3]

Input 3:
    A = [1, 1, 5]

Output 3:
    [1, 5, 1]

Input 4:
    A = [20, 50, 113]

Output 4:
    [20, 113, 50]
"""


def nextPermutation(A):
    n = len(A)
    i = n - 1
    while i > 0:
        if A[i] < A[i - 1]:
            i -= 1
        else:
            break
    if i < 1:
        A.sort()
        return A
    idx = n - 1
    while idx >= i:
        if A[idx] > A[i - 1]:
            break
        idx -= 1
    A[i - 1], A[idx] = A[idx], A[i - 1]
    A[i:].sort()
    return A


# New  & Better Solution
class Solution:
    
    def swap(self, A, i1, i2):
        A[i1], A[i2] = A[i2], A[i1]

    def reverse(self, A, l, r):
        while l < r:
            self.swap(A, l, r)
            l += 1
            r -= 1

    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        n = len(A)
        if n == 1:
            return A
        if n == 2:
            self.swap(A, 0, 1)
            return A

        dec = n - 2
        while dec >= 0 and A[dec] >= A[dec + 1]:
            dec -= 1

        self.reverse(A, dec + 1, n - 1)
        if dec == -1:
            return A

        next_num = dec + 1
        while next_num < n and A[next_num] <= A[dec]:
            next_num += 1
        self.swap(A, dec, next_num)

        return A


ans = nextPermutation([ 444, 994, 508, 72, 125, 299, 181, 238, 354, 223, 691, 249, 838, 890, 758, 675, 424, 199, 201, 788, 609, 582, 979, 259, 901, 371, 766, 759, 983, 728, 220, 16, 158, 822, 515, 488, 846, 321, 908, 469, 84, 460, 961, 285, 417, 142, 952, 626, 916, 247, 116, 975, 202, 734, 128, 312, 499, 274, 213, 208, 472, 265, 315, 335, 205, 784, 708, 681, 160, 448, 365, 165, 190, 693, 606, 226, 351, 241, 526, 311, 164, 98, 422, 363, 103, 747, 507, 669, 153, 856, 701, 319, 695, 52 ])
print ans