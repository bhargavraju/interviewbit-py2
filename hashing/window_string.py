"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T
in linear time complexity. Note that when the count of a character C in T is N,
then the count of C in minimum window in S should be at least N.

Example :
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).
"""


# @param A : string
# @param B : string
# @return a strings
def minWindow(A, B):
    from collections import defaultdict
    count_dict = defaultdict(int)
    for char in B:
        count_dict[char] += 1

    st = 0
    end = 0
    remaining = len(B)
    min_st = 0
    min_len = len(A) + 1

    n = len(A)
    while end < n:
        if count_dict[A[end]] > 0:
            remaining -= 1

        count_dict[A[end]] -= 1

        while remaining == 0:
            if end - st + 1 < min_len:
                min_len = end - st + 1
                min_st = st

            count_dict[A[st]] += 1
            if count_dict[A[st]] > 0:
                remaining += 1
            st += 1

        end += 1

    if min_len == len(A) + 1:
        return ""

    return A[min_st:min_st + min_len]
