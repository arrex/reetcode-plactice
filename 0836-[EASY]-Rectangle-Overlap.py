from typing import List


class Solution:
    """
    Intuition:
        For there to be overlap, the rectangles need to overlap both
        on the x-axis and the y-axis.

        It is easier to write the condition for no overlap then to
        write all the conditions where there would be overlap.

    Runtime:
        O(1).

    Memory:
        O(1).
    """

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # unpack: left, bottom, right, top
        l1, b1, r1, t1 = rec1
        l2, b2, r2, t2 = rec2

        # no overlap along x-axis
        x = l1 >= r2 or r1 <= l2
        # no overlap along y-axis
        y = t1 <= b2 or b1 >= t2

        # presence of overlap = overlap along x-axis and overlap along y-axis
        # x = no overlap along x-axis, not x = overlap x-axis
        return not x and not y
