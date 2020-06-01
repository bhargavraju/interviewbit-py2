"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:
Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
from functools import cmp_to_key


# Python 2
# @param A : tuple of integers
# @return a strings
def largestNumberPy2(A):
    A = map(str, A)
    res = ''.join(sorted(A, cmp=lambda a, b: cmp(a + b, b + a), reverse=True))
    res = res.lstrip('0')
    return res if res else '0'


# Python 3
# @param A : tuple of integers
# @return a strings
def largestNumberPy3(A):
    A = list(map(str, A))
    A.sort(key=cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
    res = ''.join(A)
    res = res.lstrip('0')
    return res if res else '0'
