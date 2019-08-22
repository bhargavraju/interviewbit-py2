def romanToInt(self, A):
    ref = {'X': 10, 'V': 5, 'I': 1, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in xrange(len(A)):
        cur = ref[A[i]]
        if i + 1 < len(A) and cur < ref[A[i + 1]]:
            res -= cur
        else:
            res += cur

    return res
