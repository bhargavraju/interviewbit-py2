"""
Given a string A representing an absolute path for a file (Unix-style).
Return the string A after simplifying the absolute path.
Absolute path always begins with '/' (root directory)

Refer : https://www.geeksforgeeks.org/simplify-directory-path-unix-like/
"""


def simplifyPath(A):
    stack = []
    A = A.split('/')
    for a in A:
        if a == '..':
            if len(stack) > 0:
                stack.pop()
        elif a == '.':
            continue
        elif len(a) != 0:
            stack.append(a)
    return '/' + '/'.join(stack)


test = "/../"
print simplifyPath(test)
