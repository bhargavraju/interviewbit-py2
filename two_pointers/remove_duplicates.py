"""
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
"""


def remove_duplicates(A):
    i = 0
    while i < len(A):
        j = i + 1
        while j < len(A) and A[i] == A[j]:
            j += 1
        del A[i + 1:j]
        i += 1
    return len(A)
