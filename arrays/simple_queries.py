import math


def productDivisors(n):
    i = 1
    result = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n / i == i:
                result = result * i,
            else:
                result = result * i * (n // i)
        i = i + 1
    return result


# @param A : list of integers
# @param B : list of integers
# @return a list of integers
def solve(A, B):
    n = len(A)
    g = []
    for i in range(n):
        max_elem = A[i]
        j = i
        while j < n:
            max_elem = max(max_elem, A[j])
            g.append(max_elem)
            j += 1

    g = [productDivisors(num) for num in g]
    g.sort(reverse=True)

    result = []
    for el in B:
        result.append(g[el])

    return result


test_a = [15, 87, 65, 66, 50, 75, 51, 26, 39, 54, 50, 92]
test_b = [50, 10, 39, 5, 59, 51, 35, 26, 78, 2, 27, 25, 58, 7, 39, 20, 2, 54, 4, 18, 54, 61, 1, 42, 73]
result = solve(test_a, test_b)
print result
