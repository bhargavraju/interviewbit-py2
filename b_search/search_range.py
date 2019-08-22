def get_range(A, n, i, B):
    left,right = i,i
    lmin,lmax = 0,i
    rmin,rmax = i,n-1
    while lmin <= lmax:
        lmid = (lmin+lmax)//2
        if A[lmid] == B and (lmid == 0 or A[lmid-1] < A[lmid]):
            left = lmid
            break
        elif A[lmid] < B:
            lmin = lmid+1
        else:
            lmax = lmid-1
    while rmin <= rmax:
        rmid = (rmin+rmax)//2
        if A[rmid] == B and (A[rmid+1] > A[rmid] or rmid == n-1):
            right = rmid
            break
        elif A[rmid] > B:
            rmax = rmid-1
        else:
            rmin = rmid+1
    return [left, right]


def searchRange(A, B):
    n = len(A)
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == B:
            return get_range(A, n, mid, B)
        elif A[mid] < B:
            l = mid + 1
        else:
            r = mid - 1
    return [-1, -1]


ans = searchRange([1, 2, 6, 9, 9], 2)
print ans
