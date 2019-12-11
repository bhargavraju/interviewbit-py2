"""
Given a string s, partition s such that every string of the partition is a palindrome.
Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
 [
    ["a","a","b"]
    ["aa","b"],
  ]

In the given example,
["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""
import copy


# @param A : string
# @return a list of list of strings
def partition(A):
    def combine(string, temp, res):
        n = len(string)
        if n == 0:
            # In Python, lists are passed by reference that is why it is needed to copy first and then append
            res.append(copy.deepcopy(temp))
            return
        for i in range(n):
            curr_part = string[:i + 1]
            if palindrome(curr_part):
                # Current approach reuses the same 'temp' list reference with efficient memory usage
                # Without the append and pop we can just call combine with (temp + [curr_part])
                # which creates and passes a new list. In that case there is no need for deep copy in the base case.
                temp.append(curr_part)
                combine(string[i + 1:], temp, res)
                temp.pop()

    def palindrome(string):
        return string == string[::-1]

    res = []
    combine(A, [], res)
    return res
