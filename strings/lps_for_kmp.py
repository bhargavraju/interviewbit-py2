# Returns longest proper suffix array for string pattern.
# Each lps_array[i] is the length of the longest proper prefix
# which is equal to suffix for pattern ending at character i.
# Proper means that whole string cannot be prefix or suffix.
#
# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/


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


s = "aaacaaaa"
print(calc_lps(s))
