"""
Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

Example:

Input:
1 2 3
4 5 6
7 8 9

Return the following :
[
  [1],
  [2, 4],
  [3, 5, 7],
  [6, 8],
  [9]
]

Input :
1 2
3 4

Return the following  :
[
  [1],
  [2, 3],
  [4]
]

"""


# @param A : list of list of integers
# @return a list of list of integers
def diagonal(A):
    n = len(A)
    result = []
    for layer in range(2 * n - 1):
        j = min(layer, n - 1)
        i = layer - j
        curr = []
        while 0 <= i < n and 0 <= j < n:
            curr.append(A[i][j])
            i += 1
            j -= 1
        result.append(curr)
    return result


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = diagonal(test)
print ans
