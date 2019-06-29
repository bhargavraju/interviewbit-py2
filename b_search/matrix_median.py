def count(A, e):  # number of elements smaller than e in A
    cnts = 0
    for elem in A:
        # cnts += bisect_right(elem, e)
        # This code is same as using bisect_right
        low = 0
        high = len(elem)
        while low < high:
            mid = (low+high)/2
            if elem[mid] <= e:
                low = mid+1
            else:
                high = mid
        cnts += low
    return cnts


# @param A : list of list of integers
# @return an integer
def findMedian_myver(A):
    m, n = len(A), len(A[0])
    c = (m*n)/2 + 1  # median is min number for which cnts>=c
    low, high = A[0][0], A[0][n-1]
    for i in range(m):
        low = min(A[i][0], low)
        high = max(A[i][n-1], high)
    while low <= high:
        mid = (low+high)/2
        cs = count(A, mid)
        if cs >= c:
            high = mid-1
            answer = mid
        else:
            low = mid+1
    return answer


def findMedian_org(A):
    c = (len(A) * len(A[0])) / 2 + 1  # median is min number for which cnts>=c
    low = 0
    high = 2 ** 31
    while low < high:
        mid = (low + high) / 2
        cs = count(A, mid)
        if cs < c:
            low = mid + 1
        else:
            high = mid
    return low


arr = [[1, 3, 5], [3, 6, 7], [8, 10, 11]]
ans1 = findMedian_org(arr)
ans2 = findMedian_myver(arr)
print ans1, ans2
