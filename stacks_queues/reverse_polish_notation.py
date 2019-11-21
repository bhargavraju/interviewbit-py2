"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Input 1:
    A =   ["2", "1", "+", "3", "*"]
Output 1:
    9
Explaination 1:
    starting from backside:
    *: ( )*( )
    3: ()*(3)
    +: ( () + () )*(3)
    1: ( () + (1) )*(3)
    2: ( (2) + (1) )*(3)
    ((2)+(1))*(3) = 9

Refer: https://danishmujeeb.com/blog/2014/12/parsing-reverse-polish-notation-in-python/
"""


def evalRPN(A):
    stack = []
    for el in A:
        if el in ['+', '-', '*', '/']:
            second = stack.pop()
            first = stack.pop()
            if el == '+':
                new = int(first) + int(second)
            elif el == '-':
                new = int(first) - int(second)
            elif el == '*':
                new = int(first) * int(second)
            else:
                new = int(first) // int(second)
            stack.append(str(new))
        else:
            stack.append(el)
    return stack.pop()
