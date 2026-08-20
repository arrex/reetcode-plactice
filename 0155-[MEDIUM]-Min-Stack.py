import math


class MinStack:
    """
    Intuition:
        To ensure efficient retrieval of the minimum value, we can design
        a second stack called minStack. This minStack stores the minimum
        value up until its respective element in self.stack.

        For example, if we push 1 onto the stack, then we also push 1 onto
        minStack since 1 is the smallest element encountered up to this point.
        If we then push 2 onto the stack, we still push 1 onto the minStack
        since 1 is still the smallest. Then, if we push 0 onto the stack, then
        we now change the minimum value to 0 and push 0 onto the minStack as
        well.

        Whenever we pop an element, we update the current minimum value to
        either the next top-most element on the minStack. In the case minStack
        is now empty, we reset it to math.inf such that the next element will
        automatically become the new minimum.

    Runtime:
        O(1) for all methods.

    Memory:
        O(n) since we keep 2 stacks.
    """

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = math.inf

    def push(self, val: int) -> None:
        self.currMin = min(self.currMin, val)

        self.stack.append(val)
        self.minStack.append(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

        # reset currMin
        self.currMin = self.minStack[-1] if self.minStack else math.inf

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
