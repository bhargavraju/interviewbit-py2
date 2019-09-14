# @param A : string
# @param B : string
# @return a strings


def multiply(A, B):
    ans = ['0'] * (len(A) + len(B) + 1)
    pos = 0
    for i in range(len(B)):
        k = int(B[-(i + 1)])
        carr = 0
        pos -= 1
        for j in range(len(A)):
            temp = k * int(A[-(j + 1)]) + int(ans[pos - j]) + carr
            ans[pos - j] = str(temp % 10)
            carr = temp / 10
        ans[pos - len(A)] = str(carr)
    ret = ''.join(ans).lstrip('0')
    if ret == '':
        ret = '0'
    return ret
