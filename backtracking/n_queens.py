"""
The n queens puzzle is the problem of placing n queens on an nxn board such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n queens placement, where 'Q' and '.' indicate a queen and
empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


# @param A : integer
# @return a list of list of strings
def solveNQueens(A):
    fin = []

    def solve(A, res):
        if len(res) == A:
            fin.append(res)
        for i in range(1, A + 1):
            if not attack(res, i):
                solve(A, res + [i])

    solve(A, [])
    return [["." * (i - 1) + "Q" + "." * (A - i) for i in cols] for cols in fin]


def attack(prev, pos):
    for i in range(len(prev)):
        if prev[i] == pos or abs(len(prev) - i) == abs(prev[i] - pos):  # Vertical and diagonal check
            return True
    return False
