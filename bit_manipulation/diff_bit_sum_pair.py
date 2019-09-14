def cntBits(A):
    MODU = 10 ** 9 + 7
    maxi, n = max(A), len(A)
    mask = 1
    res = 0
    while mask <= maxi:
        x = sum(1 for a in A if a & mask)
        mask <<= 1

    return (2 * res) % MODU
