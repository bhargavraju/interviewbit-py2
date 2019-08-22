def compareVersion(A, B):
    a = A.split('.')
    b = B.split('.')
    l_a, l_b = len(a), len(b)
    i = 0
    while i < l_a and i < l_b:
        if int(a[i]) > int(b[i]):
            return 1
        elif int(a[i]) < int(b[i]):
            return -1
        i += 1
    if i < l_a:
        while i < l_a:
            if int(a[i]) > 0:
                return 1
            i += 1
    if i < l_b:
        while i < l_b:
            if int(b[i]) > 0:
                return -1
            i += 1
    return 0


A = "1.0"
B = "1"
ans = compareVersion(A, B)
print ans

# Simpler implementation


def compareVersion(A, B):
    for a, b in map(None, A.split('.'), B.split('.')):
        a, b = int(a or 0), int(b or 0)
        if a > b:
            return 1
        if a < b:
            return -1
    return 0
