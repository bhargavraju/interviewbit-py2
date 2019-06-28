def sqrt(A):
    if A == 0 or A == 1:
        return A
    l, r = 1, A
    while l <= r:
        mid = (l + r) // 2
        sqr = mid ** 2
        if sqr == A:
            return mid
        elif sqr < A:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    return ans


# floor of the root value
ans = sqrt(7)
print ans
