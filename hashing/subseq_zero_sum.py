"""
Find the largest continuous sequence in a array which sums to zero.

Example:
Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}

 NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
"""


# @param A : list of integers
# @return a list of integers
def lszero(A):
    sum_dict = {0: -1}
    # this dict initiation is to cover the cases where
    # (i) only one element is 'zero' and no other subsequence sum will be zero
    # (ii) subsequence with sum zero starts from the first element (which cannot be detected otherwise)
    total = 0
    maxLCS, maxi, maxj = 0, -1, -1

    for i, val in enumerate(A):
        total += val
        if total in sum_dict:
            if maxLCS < i - sum_dict[total]:
                maxLCS = i - sum_dict[total]
                maxi = sum_dict[total] + 1
                maxj = i + 1
        else:
            sum_dict[total] = i

    return A[maxi: maxj] if maxLCS else []
