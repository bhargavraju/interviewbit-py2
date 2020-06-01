"""
You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, ... SN
In a single operation, you can choose two indices L and R such that 1 <= L <= R <= N and
flip the characters SL, SL+1, .... SR. By flipping, we mean change character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised.
If you don't want to perform any operation, return an empty array. Else, return an array consisting of two elements
denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

Notes:
Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d.

For example,
S = 010
Pair of [L, R] | Final string
_______________|_____________
[1 1]          | 110
[1 2]          | 100
[1 3]          | 101
[2 2]          | 000
[2 3]          | 001

We see that two pairs [1, 1] and [1, 3] give same number of 1s in final string. So, we return [1, 1].

Another example,
If S = 111

No operation can give us more than three 1s in final string. So, we return empty array [].
"""

from sys import maxint


# @param A : string
# @return a list of integers
def flip(A):
    arr = list(A)
    count = 0
    max_count = -maxint-1
    l = 0
    ans = None
    for i in xrange(len(arr)):
        if arr[i] == 0:
            count += 1
            if count > max_count:
                max_count = count
                ans = [l, i]
        elif arr[i] == 1:
            count -= 1
            if count < 0:
                count = 0
                l = i + 1
    if max_count == -maxint-1:
        return []
    return map(lambda x: x+1, ans)
