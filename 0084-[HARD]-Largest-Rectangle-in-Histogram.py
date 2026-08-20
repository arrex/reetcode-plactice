from typing import List


class Solution:
    """
    Intuition:
        The key idea is that for each bar, we need to know how far it can extend
        to the left and right before hitting a shorter bar. Instead of checking
        all possible widths (which would be O(n^2)), we use a stack to keep track
        of increasing bar heights with their starting indices. When we encounter
        a shorter bar, we know it bounds the bars in the stack, so we pop them
        and calculate the maximum rectangle they could have formed, using the
        current index as the right boundary.

    Runtime:
        Each element is pushed onto the stack at most once. Similarly, each element
        is popped from the stack at most once. This leads to an overall runtime of
        O(n).

    Memory:
        O(n) for the stack.
    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # hold pairs: (ix, height)
        res = 0
        N = len(heights)

        for i, h in enumerate(heights):
            startIx = i

            while stack and stack[-1][1] > h:
                ix, height = stack.pop()

                # check if popped height could have been largest rectangle
                area = height * (i - ix)
                res = max(res, area)

                startIx = ix

            stack.append((startIx, h))

        for i, h in stack:
            area = h * (N - i)
            res = max(res, area)

        return res
