def search(A, B):
    n = len(A)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return mid
        elif A[l] <= A[mid]:
            if A[l] <= B < A[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if A[mid] < B <= A[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
