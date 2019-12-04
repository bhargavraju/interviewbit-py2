"""
Implement pow(A, B) % C.
In other words, given A, B and C, find (A^B)%C

Input : A = 2, B = 3, C = 3
Return : 2
2^3 % 3 = 8 % 3 = 2

Hint: (axb)%c = ((a%c)x(b%c))%c
"""


# @param A : integer
# @param B : integer
# @param C : integer
# @return an integer
def Mod(A, B, C):
    if B == 0:
        return 0 if A == 0 else 1
    elif B % 2 == 0:
        y = Mod(A, B / 2, C)
        return y * y % C
    else:
        return ((A % C) * Mod(A, B - 1, C)) % C
