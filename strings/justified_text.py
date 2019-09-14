# @param A : list of strings
# @param B : integer
# @return a list of strings


def fullJustify( A, B):
    n = len(A)
    ans = []
    i = 0
    while i < n:
        l = k = 0
        # k represents how many words should be taken to form the required string.
        # l represents the length of characters(other than " ") in the string.
        while (i + k) < n and l + len(A[i + k]) <= B - k:
            l += len(A[i + k])
            k += 1

        tmp = A[i]
        for j in range(k - 1):
            if i + k == n:
                # if last line and more words to go.
                tmp += " "
            else:
                # for evenly distributed spaces.
                tmp += " " * ((B - l) // (k - 1) + int(j < (B - l) % (k - 1)))
            tmp += A[i + j + 1]

        # Remaining spaces in the last line.
        tmp += " " * (B - len(tmp))
        ans.append(tmp)
        i += k
    return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16

ans = fullJustify(words, L)
