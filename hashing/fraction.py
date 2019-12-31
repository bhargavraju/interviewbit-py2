"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

Example :
Given numerator = 1, denominator = 2, return "0.5"
Given numerator = 2, denominator = 1, return "2"
Given numerator = 2, denominator = 3, return "0.(6)"
"""


# @param A : integer
# @param B : integer
# @return a strings
def fractionToDecimal(A, B):
    if A == 0:
        return '0'

    res = ''
    res += '-' if (A < 0) ^ (B < 0) else ''

    A = abs(A)
    B = abs(B)

    int_part = A // B
    res += str(int_part)

    rem = A % B
    if rem == 0:
        return res
    res += '.'

    decimal_part = ''
    rem_values = {}
    index = 0
    repeating_index = 0
    rec = False
    while rem != 0:
        if rem in rem_values:
            repeating_index = rem_values[rem]
            rec = True
            break
        else:
            rem_values[rem] = index

        index += 1
        rem = rem * 10
        decimal_part += str(rem // B)
        rem = rem % B

    if rec:
        decimal_part = decimal_part[:repeating_index] + '(' + decimal_part[repeating_index:] + ')'
    return res + decimal_part
