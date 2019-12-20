"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2.
 Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function.
Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum.
If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.
"""


# @param A : tuple of integers
# @param B : integer
# @return a list of integers
def twoSum(A, B):
    n = len(A)
    store = {}
    for i in range(n):
        if B-A[i] in store:
            return [store[B-A[i]]+1, i+1]
        elif A[i] not in store:
            store[A[i]] = i
    return []


test = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
ans = twoSum(test, -3)
print ans == [4, 8]
