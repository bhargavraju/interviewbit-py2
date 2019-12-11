"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.

Example :
Input to your program will be
[[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]

and we would expect your program to modify the above array of array of characters to
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]
"""


# @param A : list of list of chars
# @return nothing
def solveSudoku(A):
    solver(A)


def solver(A):
    for i in range(9):
        for j in range(9):
            if A[i][j] != '.':
                continue
            for num in range(1, 10):
                if is_safe(A, i, j, num):
                    A[i][j] = str(num)
                    if solver(A):
                        return True
                    else:
                        A[i][j] = '.'
            return False
    return True


def is_safe(A, i, j, num):
    for idx in range(9):
        if A[i][idx] == str(num) or A[idx][j] == str(num):
            return False
    box_x, box_y = i - (i % 3), j - (j % 3)
    for x in range(box_x, box_x + 3):
        for y in range(box_y, box_y + 3):
            if A[x][y] == str(num):
                return False
    return True
