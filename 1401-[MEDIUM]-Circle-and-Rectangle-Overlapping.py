from math import sqrt


class Solution:
    """
    Intuition:
        The idea is to traverse the perimeter of the rectangle and verify
        the distance between each point along the perimeter and the center
        of the circle. If the distance is less than or eq to the radius,
        then we have overlap. The only edge case we need to account for is
        when the circle is enclosed within the rectangle.

    Runtime:
        Let w be the widt, and h be the height of the rectangle.

        Our runtime is O(h + w).

    Memory:
        O(1).
    """

    def checkOverlap(
        self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int
    ) -> bool:
        # helper
        def cartesian_dist(x1, y1, x2, y2):
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        # circle enclosed within rectangle
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        # scan height edges
        for i in range(y2 - y1 + 1):
            if (
                cartesian_dist(xCenter, yCenter, x1, y1 + i) <= radius
                or cartesian_dist(xCenter, yCenter, x2, y1 + i) <= radius
            ):
                return True

        # scan width edges
        for i in range(x2 - x1 + 1):
            if (
                cartesian_dist(xCenter, yCenter, x1 + i, y1) <= radius
                or cartesian_dist(xCenter, yCenter, x1 + i, y2) <= radius
            ):
                return True

        return False
