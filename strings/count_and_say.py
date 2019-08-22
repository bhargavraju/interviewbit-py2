# @param A : integer
# @return a strings


def count_and_say(A):
    if A == 1:
        return 1
    prev = str(1)
    for i in range(2, A + 1):
        j, ch, cnt = 0, prev[0], 0
        curr = ''
        while j < len(prev):
            if prev[j] == ch:
                j += 1
                cnt += 1
                continue
            else:
                curr += str(cnt) + ch
                ch = prev[j]
                cnt = 0
        curr += str(cnt) + ch
        prev = curr
    return prev
