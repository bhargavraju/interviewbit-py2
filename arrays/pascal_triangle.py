"""
Given numRows, generate the first numRows of Pascal's Triangle.

Pascal's Triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""


def solve(A):
    ans = []
    for i in range(A):
        sol = [1]
        if ans:
            prev = ans[-1]
            for j in range(len(prev) - 1):
                sol.append(prev[j] + prev[j + 1])
        if i != 0:
            sol.append(1)
        ans.append(sol)
    return ans


ans = solve(4)
print ans


# @param A : integer
# @return a list of list of integers
def solve(A):
    if A == 0:
        return []
    result = [[1]]
    for num in range(1, A):
        prev = result[-1]
        l = len(prev)
        new_list = [1]
        for i in range(l - 1):
            new_list.append(prev[i] + prev[i + 1])
        new_list.append(1)
        result.append(new_list)
    return result
