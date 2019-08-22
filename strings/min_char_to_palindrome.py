"""
Given an string A. The only operation allowed is to insert characters in the beginning of the string.

Find how many minimum characters are needed to be inserted to make the string a palindrome string.
"""


def calc_lps(arr):
    n = len(arr)
    lps = [0] * n
    i, j = 1, 0
    while i < n:
        if arr[i] == arr[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        lps_arr = calc_lps(A + '$' + A[::-1])
        return len(A) - lps_arr[-1]
