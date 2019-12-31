"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
"""


# @param A : string
# @param B : tuple of strings
# @return a list of integers
def findSubstring(A, B):
    n = len(B)
    if n == 0:
        return []
    k = len(B[0])
    if n * k > len(A):
        return []
    ans = []
    for i in range(len(A)):
        substr = A[i:i + k]
        if substr in B:
            words = list(B)
            words.remove(substr)
            new_idx = i + k
            for j in range(n - 1):
                new_word = A[new_idx:new_idx + k]
                if new_word in words:
                    words.remove(new_word)
                    new_idx += k
                else:
                    break
            else:
                ans.append(i)
    return ans
