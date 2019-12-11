"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""


# @param A : integer
# @return a list of strings
def generateParenthesis(A):
    res = []
    generate(A, 0, 0, '', res)
    return res


def generate(n, op, cl, curr, res):
    if cl == n:
        res.append(curr)
    else:
        if op < n:
            generate(n, op + 1, cl, curr + '(', res)
        if op > cl:
            generate(n, op, cl + 1, curr + ')', res)
