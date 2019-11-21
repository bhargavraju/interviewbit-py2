"""
Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'
Check whether A has redundant braces or not. Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.
Refer: https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/
"""


def braces(A):
    stack = []
    for ch in A:
        if ch == ')':
            top = stack[-1]
            stack.pop()
            flag = True
            while top != '(':
                if top == '+' or top == '-' or top == '*' or top == '/':
                    flag = False
                top = stack[-1]
                stack.pop()
            if flag:
                return 1
        else:
            stack.append(ch)
    return 0
