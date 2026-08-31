from math import inf
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    Intuition:
        We scan the linked list by looking at sets of 3 nodes (prev, curr, next) to
        find all the local maxima and minima. We record each critical point's position.

        Then, the maximum distance is simply the distance between the leftmost and
        rightmost critical points.

        And the minimum distance is the smallest distance between adjacent critical
        points.

    Runtime:
        O(n) to find the positions of all critical points.

        O(1) to compute max distance.

        We have at most O(n // 2) critical points, meaning finding the min distance
        takes O(n // 2) ~ O(n) time.

        Overall, O(n) runtime.

    Memory:
        O(n // 2) ~ O(n) to store all the positions of all the critical points.
    """

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # base case
        if not head:
            return [-1, -1]

        pos = 1
        crit = []
        prev, curr = head, head.next

        while curr and curr.next:
            next = curr.next

            if curr.val < prev.val and curr.val < next.val:
                crit.append(pos)

            if curr.val > prev.val and curr.val > next.val:
                crit.append(pos)

            prev, curr = curr, next
            pos += 1

        # base case
        if len(crit) < 2:
            return [-1, -1]

        maxDist = crit[-1] - crit[0]

        # check all adj pairs of crit pts
        minDist = inf
        for l in range(len(crit) - 1):
            r = l + 1
            minDist = min(minDist, crit[r] - crit[l])

        return [minDist, maxDist]


class Solution2:
    """
    Intuition:
        We can slightly refine solution 1 by realizing that the max distance only
        cares about the first and last critical pts and the min distance only cares
        about adjacent crit pts.

        As such, we do not need to track all critical points, only the ones we care
        about. This eliminates the second pass over all pairs of crit pts to find
        min distance.

    Runtime:
        Still O(n).

    Memory:
        O(1).
    """

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return [-1, -1]

        # we only care about the previous crit pt for min dist
        prevCrit, minDist = -inf, inf
        # we only care about first and last crit pts for max dist
        firstCrit, lastCrit = None, None

        pos = 1
        prev, curr = head, head.next
        while curr and curr.next:
            next = curr.next

            if (curr.val < prev.val and curr.val < next.val) or (
                curr.val > prev.val and curr.val > next.val
            ):
                if not firstCrit:
                    firstCrit = pos

                minDist = min(minDist, pos - prevCrit)
                prevCrit = pos
                lastCrit = pos

            prev, curr = curr, next
            pos += 1

        # either no crit pts or only 1 crit pt
        if not firstCrit or firstCrit == lastCrit:
            return [-1, -1]

        # compute max dist
        maxDist = lastCrit - firstCrit

        return [minDist, maxDist]
