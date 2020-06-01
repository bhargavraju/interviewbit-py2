"""
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

Input Format:
The first and the only argument contains an integer, A.

Output Format:
Return a 2-d matrix of size A x A satisfying the spiral order.

Constraints:
1 <= A <= 1000

Examples:

Input 1:
    A = 3

Output 1:
    [   [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]   ]

Input 2:
    4

Output 2:
    [   [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]   ]
"""


# @param A : integer
# @return a list of list of integers
def generateMatrix(A):
    result = [[0 for x in range(A)] for y in range(A)]
    l, r, t, b = 0, A - 1, 0, A - 1
    direction = 0
    element = 1
    while l <= r and t <= b:
        if direction == 0:
            for i in range(l, r + 1):
                result[t][i] = element
                element += 1
            t += 1
        elif direction == 1:
            for i in range(t, b + 1):
                result[i][r] = element
                element += 1
            r -= 1
        elif direction == 2:
            for i in range(r, l - 1, -1):
                result[b][i] = element
                element += 1
            b -= 1
        else:
            for i in range(b, t - 1, -1):
                result[i][l] = element
                element += 1
            l += 1
        direction = (direction + 1) % 4
    return result
