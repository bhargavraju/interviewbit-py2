from sys import maxint
# @param A : list of integers
# @return an integer


def max_arr(A):  # Brute force
    max_diff = -maxint-1
    steps = 1
    n = len(A)
    while(steps < n):
        for i in range(0, n):
            if i + steps < n:
                diff = abs(A[i] - A[i+steps]) + steps
                if diff > max_diff:
                    max_diff = diff
        steps += 1
    return max_diff


ans = max_arr([-70, -64, -6, -56, 64, 61, -57, 16, 48, -98])
print ans

"""
    Two cases (A[i] + i) - (A[j] + j) and (A[i] - i) - (A[j] - j)
    Find min, max values of A[i] + i, A[i] - i for entire array
    subtract min from max, compare values of both cases
    
"""