"""
Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

Input Format:
The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.

Output Format:
Return a 2-d matrix that satisfies the given conditions.

Constraints:
1 <= N, M <= 1000
0 <= A[i][j] <= 1

Examples:

Input 1:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]   ]

Output 1:
    [   [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1]   ]

Input 2:
    [   [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]   ]

Output 2:
    [   [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]   ]
"""


# With O(M+N) memory
# @param A : list of list of integers
# @return the same list modified
def setZeroes(A):
    rows = set()
    cols = set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in rows:
        for j in range(len(A[0])):
            A[i][j] = 0
    for j in cols:
        for i in range(len(A)):
            A[i][j] = 0
    return A


# With O(1) memory
# @param A : list of list of integers
# @return the same list modified
def setZeroesNew(A):
    m = len(A)
    n = len(A[0])
    R = 0 if 0 in A[0] else 1
    C = 0 if 0 in [A[i][0] for i in range(m)] else 1
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                A[i][0] = 0
                A[0][j] = 0
    for i in range(1, m):
        if A[i][0] == 0:
            for j in range(n):
                A[i][j] = 0
    for j in range(1, n):
        if A[0][j] == 0:
            for i in range(m):
                A[i][j] = 0
    if R == 0:
        for j in range(n):
            A[0][j] = 0
    if C == 0:
        for i in range(m):
            A[i][0] = 0
    return A
