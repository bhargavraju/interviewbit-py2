"""
Given a string,
find the length of the longest substring without repeating characters.

Example:
The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
For "bbbbb" the longest substring is "b", with the length of 1.
"""


# @param A : string
# @return an integer
def lengthOfLongestSubstring(A):
    n = len(A)
    i = j = 0
    char_store = {}
    max_length = 0
    while j < n:
        if A[j] in char_store and char_store[A[j]] >= i:  # Move only if the duplicate position is within the substring
            i = char_store[A[j]] + 1
        else:
            max_length = max(max_length, j - i + 1)
        char_store[A[j]] = j
        j += 1
    return max_length
