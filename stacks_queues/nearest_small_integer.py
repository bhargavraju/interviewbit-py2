"""
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an
index smaller than i.

G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]

Input 1:
    A = [4, 5, 2, 10, 8]
Output 1:
    G = [-1, 4, -1, 2, 2]

Input 2:
    A = [3, 2, 1]
Output 2:
    [-1, -1, -1]
"""


def prevSmaller(A):
    stack = []
    result = []
    for el in A:
        while len(stack) > 0 and stack[-1] >= el:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(el)
    return result
