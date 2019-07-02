# @param A : integer
# @param B : integer
# @param C : list of integers
# @return an integer


def paint(A, B, C):
    l = max(C)
    r = sum(C)
    ans = r
    while l <= r:
        mid = (l+r)//2
        painter = 1
        load = 0
        for board in C:
            load += board
            if load > mid:
                load = board
                painter += 1
        if painter <= A:
            r = mid-1
            ans = mid
        else:
            l = mid+1
    return (ans*B)%10000003
