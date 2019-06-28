def get_count(A, idx, B, n):
    left, right = idx, idx
    if idx != 0 and A[idx - 1] == A[idx]:
        l, r = 0, idx - 1
        while l <= r:
            mid = (l + r) // 2
            if (mid == 0 or A[mid - 1] < A[mid]) and A[mid] == B:
                left = mid
                break
            elif A[mid] < B:
                l = mid + 1
            else:
                r = mid - 1
    if idx != n - 1 and A[idx] == A[idx + 1]:
        l, r = idx + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            if (mid == n - 1 or A[mid + 1] > A[mid]) and A[mid] == B:
                right = mid
                break
            elif A[mid] > B:
                r = mid - 1
            else:
                l = mid + 1
    return right - left + 1


def findCount(A, B):
    n = len(A)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return get_count(A, mid, B, n)
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1
    return 0
