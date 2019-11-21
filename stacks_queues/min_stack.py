"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) - Push element x onto stack.
pop() - Removes the element on top of the stack.
top() - Get the top element.
getMin() - Retrieve the minimum element in the stack.

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = None

    # @param x, an integer
    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.mini = x
        else:
            if x >= self.mini:
                self.stack.append(x)
            else:
                el = 2 * x - self.mini
                self.stack.append(el)
                self.mini = x

    # @return nothing
    def pop(self):
        if not self.stack:
            return
        x = self.stack.pop()
        if x < self.mini:
            self.mini = 2 * self.mini - x

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        else:
            top = self.stack[-1]
            if top < self.mini:
                return self.mini
            else:
                return top

    # @return an integer
    def getMin(self):
        return self.mini if self.stack else -1
