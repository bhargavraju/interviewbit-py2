# @param A : integer
# @param B : integer
# @return an integer


def divide(A, B):
    sign = -1 if ((A < 0) ^ (B < 0)) else 1

    divident = abs(A)
    divisor = abs(B)

    temp = 0
    quotient = 0

    for idx in xrange(31, -1, -1):
        if (temp + (divisor << idx)) <= divident:
            temp += (divisor << idx)
            quotient |= (1 << idx)

    quotient *= sign
    if quotient > (2 ** 31 - 1):
        return 2 ** 31 - 1
    elif quotient < -2 ** 31:
        return -2 ** 31
    else:
        return quotient