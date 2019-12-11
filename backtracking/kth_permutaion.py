"""
The set [1,2,3,....n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3 ) :

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.
For example, given n = 3, k = 4, ans = "231"
"""
from math import factorial as fact


# @param A : integer
# @param B : integer
# @return a strings
def getPermutation(A, B):
    digits = [str(i) for i in range(1, A + 1)]
    return recurse(digits, B - 1)


def recurse(digits, k):
    n = len(digits)
    if n == 1:
        return digits[0]
    di = k / fact(n - 1)
    k2 = k % fact(n - 1)
    d = digits[di]
    digits = digits[:di] + digits[di + 1:]
    return d + recurse(digits, k2)


n, k = 3, 4
ans = getPermutation(n, k)
print ans
